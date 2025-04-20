```markdown
# 🧠 AI Prototype Development for Multimodal Social Support Applications

This repository contains a complete Flask-based AI prototype application developed for multimodal social support. It includes all relevant source code, dependencies, and setup instructions.

---

## 🚀 How to Get Started

Follow the steps below to set up and run the project locally.

---

### 🔁 1. Clone the Repository

Open your terminal or Git Bash and run:

```bash
git clone https://github.com/DeepNeuralAI313/AI-Prototype-Development-for-Multimodal-Social-Support-Applications.git
cd AI-Prototype-Development-for-Multimodal-Social-Support-Applications
```

---

### 🐍 2. Install Python 10

Make sure Python 10 is installed on your system.

If it's not installed, download and install Python 3.10 from the official website:  
🔗 https://www.python.org/downloads/release/python-3100/

Once installed, verify it:

```bash
python3.10 --version
```

---

### 🧪 3. Create Virtual Environment (Optional but Recommended)

```bash
python3.10 -m venv venv
source venv/bin/activate     # For Linux/Mac
venv\Scripts\activate        # For Windows
```

---

### 📦 4. Install Required Dependencies

Install all packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```


---

### 🛠️ 5. Add Groq API Key

In order to use the Groq model, you need to obtain an API key. Follow these steps:

1. Visit [Groq API](https://www.groq.com/) and sign up for an API key.
2. Once you have the API key, open the `app.py` file.
3. Add the API key to the environment variables or directly in the `app.py` file like this:

```python

# Groq API Key (Make sure to keep it secret)
GROQ_API_KEY = "your-groq-api-key-here"

```

Alternatively, you can use a `.env` file to store sensitive data like the API key securely.

---

---

### 🏁 6. Run the Flask App

Once everything is installed, you can start the Flask app using:

```bash
python app.py
```

By default, the app will be hosted at:  
📍 `http://127.0.0.1:5000/`

---

## 📂 Project Structure

```bash
📁 AI-Prototype-Development-for-Multimodal-Social-Support-Applications
│
├── app.py
├── requirements.txt
├── templates/
├── static/
├── ...
```

---

## 🙌 Contributing

Feel free to fork the project, open issues, or submit pull requests.

---

## 📧 Contact

Maintained by [DeepNeuralAI](https://github.com/DeepNeuralAI313)

---




