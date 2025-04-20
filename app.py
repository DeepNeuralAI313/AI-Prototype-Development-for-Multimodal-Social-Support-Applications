# Import required libraries
from flask import Flask, request, jsonify  # Flask for web framework
import os  # For file and directory operations
import time  # For time-related functions
import pandas as pd  # For data manipulation
from paddleocr import PaddleOCR  # For OCR functionality
from groq import Groq  # For LLM API access
import docx  # For DOCX file processing
import pdfplumber  # For PDF file processing
import pickle  # For loading serialized objects

# Initialize PaddleOCR with English language support and angle classification
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Initialize Groq client with API key
client = Groq(api_key="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")

# Import TensorFlow model loading function
from tensorflow.keras.models import load_model
import numpy as np

# Load pre-trained financial aid model and preprocessing tools
model = load_model("static/models/financial_aid_model.h5")
with open("static/models/preprocessing_pipeline.pkl", "rb") as f:
    tools = pickle.load(f)

# Extract preprocessing tools from loaded pickle file
scaler = tools["scaler"]  # For feature scaling
le_gender = tools["le_gender"]  # Label encoder for gender
le_prev = tools["le_prev"]  # Label encoder for previous assistance
le_emp = tools["le_emp"]  # Label encoder for employment status
le_edu = tools["le_edu"]  # Label encoder for education level

def predict_eligibility(input_data):
    """
    Predict financial aid eligibility based on input data.
    Args:
        input_data: dict containing applicant information with keys:
            'Credit_Score', 'Education_Level', 'Employment_Status', 'Income',
            'Dependents', 'Age', 'Gender', 'Previous_Assistance'
    Returns:
        bool: True if eligible, False if not eligible
    """
    # Prepare input data array
    x = np.array([[
        input_data['Credit_Score'],
        le_edu.transform([input_data['Education_Level']])[0],
        le_emp.transform([input_data['Employment_Status']])[0],
        input_data['Income'],
        input_data['Dependents'],
        input_data['Age'],
        le_gender.transform([input_data['Gender']])[0],
        le_prev.transform([input_data['Previous_Assistance']])[0]
    ]])
    
    # Normalize input features
    x_scaled = scaler.transform(x)

    # Make prediction
    prediction = model.predict(x_scaled)[0][0]
    if prediction >= 0.5:
        return True
    else:
        return False
 
def image_and_entered_id_verification(user_id, image_file):
    """
    Verify user ID by comparing entered ID with OCR-extracted ID from image.
    Args:
        user_id: string, user-entered Emirates ID
        image_file: path to ID image file
    Returns:
        tuple: (bool verification status, dict user data if verified)
    """
    # Step 1: Check if ID exists in database
    df = pd.read_csv('saudi_applicants.csv')
    if user_id not in df['Emirates_ID'].astype(str).values:
        return False, {}

    # Step 2: Perform OCR on ID image
    result = ocr.ocr(image_file, cls=True)
    extracted_text = " ".join([line[1][0] for block in result for line in block])

    # Step 3: Use LLM to extract ID from OCR text
    prompt = f"""Extract only the Emirates ID number from the following OCR text:\n\n{extracted_text}\n\nReturn only the Emirates ID. I don't want any single letter extra."""
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_completion_tokens=50,
        top_p=1,
        stream=False
    )
    llm_output = completion.choices[0].message.content.strip()

    # Compare extracted ID with user-entered ID
    if llm_output == user_id:
        user_data = df[df['Emirates_ID'].astype(str) == user_id].iloc[0].to_dict()
        return True, user_data
    else:
        return False, {}

# Initialize Flask application
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Folder to store uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create upload folder if it doesn't exist

currunt_user_id = None  # Global variable to store current user ID

@app.route('/')
def index():
    """Serve the main index page."""
    return open('templates/index.html', encoding='utf-8').read()

@app.route('/verify_id', methods=['POST'])
def verify_id():
    """Handle ID verification request."""
    user_id = request.form.get('userID')  # Get user-entered ID
    id_file = request.files.get('idUpload')  # Get uploaded ID file
   
    if user_id and id_file:
        # Save uploaded file
        id_path = os.path.join(app.config['UPLOAD_FOLDER'], id_file.filename)
        id_file.save(id_path)

        # Verify ID
        is_verified, user_data = image_and_entered_id_verification(user_id, id_path)
        global currunt_user_id
        currunt_user_id = user_id  # Store current user ID
        
        if is_verified:
            return jsonify({"status": "success", "message": "✅ ID verification successful!", "user_data": user_data})
        else:
            return jsonify({"status": "error", "message": "❌ ID verification failed!"})
    
    return jsonify({"status": "error", "message": "⚠️ Missing ID or file!"})

def image_and_entered_salary_verification(user_salary, file_path):
    """
    Verify salary by comparing entered salary with extracted salary from document.
    Args:
        user_salary: string, user-entered salary
        file_path: path to salary slip document
    Returns:
        bool: True if verification successful, False otherwise
    """
    extracted_text = ""  # Initialize text variable

    # Process PDF files
    if file_path.lower().endswith('.pdf'):
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    extracted_text += page.extract_text() + "\n"
        except Exception as e:
            print("❌ PDF reading error:", e)
            return False

    # Process DOCX files
    elif file_path.lower().endswith('.docx'):
        try:
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                extracted_text += para.text + "\n"
        except Exception as e:
            print("❌ DOCX reading error:", e)
            return False

    else:
        print("❌ Unsupported file type")
        return False

    # Prompt LLM to extract salary from document text
    prompt = f"""
        Extract only the numeric salary amount from the following salary slip content:
        \n\n{extracted_text}\n\n
        Return only the numeric salary value without currency symbols or extra text.
        ""Return only the salary."" i dont wnat any single latter extra.
    """

    try:
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_completion_tokens=50,
            top_p=1,
            stream=False
        )

        extracted_salary = completion.choices[0].message.content.strip()

        # Compare extracted salary with user-entered salary
        return str(user_salary) == extracted_salary

    except Exception as e:
        print(f"❌ LLM error: {e}")
        return False

@app.route('/submit_salary', methods=['POST'])
def submit_salary():
    """Handle salary verification request."""
    user_salary = request.form.get('userSalary')  # Get user-entered salary
    salary_file = request.files.get('salarySlip')  # Get uploaded salary slip

    if user_salary and salary_file:
        # Save uploaded file
        salary_path = os.path.join(app.config['UPLOAD_FOLDER'], salary_file.filename)
        salary_file.save(salary_path)

        # Verify salary
        is_verified = image_and_entered_salary_verification(user_salary, salary_path)
        if is_verified:
            return jsonify({"status": "success", "message": "✅ Salary verification successful!"})
        else:
            return jsonify({"status": "error", "message": "❌ Salary verification failed!"})
    
    return jsonify({"status": "error", "message": "⚠️ Missing salary or file!"})

def calculate_aid(emirates_id, csv_path='saudi_applicants.csv'):
    """
    Calculate financial aid amount based on applicant data.
    Args:
        emirates_id: string, applicant's Emirates ID
        csv_path: path to applicant data CSV file
    Returns:
        dict: Contains applicant name, ID, score, and calculated aid amount
    """
    df = pd.read_csv(csv_path)

    # Find applicant in database
    person = df[df['Emirates_ID'] == emirates_id]

    if person.empty:
        return f"Emirates ID {emirates_id} not found."

    person = person.iloc[0]

    # Initialize scoring
    score = 0
    income = person.get('Income', 0)
    dependents = person.get('Dependents', 0)
    employment = str(person.get('Employment_Status', '')).lower()
    education = str(person.get('Education_Level', '')).lower()
    previous = str(person.get('Previous_Assistance', '')).lower()
    credit_score = person.get('Credit_Score', 0)

    if not predict_eligibility(person.to_dict()):
        return {"status": "error", "message": "❌ You are not eligible for financial aid."}
    
    # Calculate score based on income
    if income < 5000:
        score += 30
    elif 5000 <= income <= 10000:
        score += 20
    else:
        score += 10

    # Calculate score based on dependents
    if dependents >= 4:
        score += 20
    elif 2 <= dependents < 4:
        score += 10

    # Calculate score based on employment status
    if employment in ['عاطل عن العمل', 'عمل حر','دوام جزئي']:
        score += 20
    elif employment in ['متقاعد']:
        score += 15
    else:
        score += 10

    # Calculate score based on education level
    if education in ['الثانوية العامة', 'بكالوريوس']:
        score += 10
    elif education in ['ماجستير']:
        score += 5

    # Calculate score based on previous assistance
    if previous == 'no':
        score += 10

    # Calculate score based on credit score
    if credit_score < 500:
        score += 10

    # Determine aid amount based on total score
    if score >= 80:
        aid_amount = 5000
    elif score >= 60:
        aid_amount = 3000
    elif score >= 40:
        aid_amount = 1500
    else:
        aid_amount = 0

    return {
        "Name": person['Name'],
        "Emirates_ID": emirates_id,
        "Score": score,
        "Aid_Amount": aid_amount
    }

@app.route('/final_submit', methods=['POST'])
def final_submit():
    """Handle final application submission."""
    time.sleep(5)  # Simulate processing delay
    global currunt_user_id
    data = calculate_aid(currunt_user_id)  # Calculate aid for current user
    print(f"📩 Final Submission Received:\n{data}")
    return jsonify({"status": "success", "message": "✅ Application submitted successfully!", "data": data})

if __name__ == '__main__':
    app.run(debug=True)  # Run Flask app in debug mode