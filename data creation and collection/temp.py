# import pandas as pd

# df = pd.read_csv('data.csv')

# Names = [
#     "أحمد المنصوري",
#     "فاطمة الزعابي",
#     "محمد الحمادي",
#     "عائشة الشامسي",
#     "حمد السويدي",
#     "مريم النعيمي",
#     "خالد العامري",
#     "نورة المزروعي",
#     "سعيد المري",
#     "لطيفة الرميثي",
#     "عبدالله العلي",
#     "هند الحساني",
#     "يوسف الكتبي",
#     "سلمى المهيري",
#     "عمر الدرعي",
#     "ريم الشامسي",
#     "ماجد الفلاسي",
#     "ليلى الطنيجي",
#     "راشد القباسي",
#     "آمنة الشيحي",
#     "ناصر الكعبي",
#     "شيخة الشامسي",
#     "فهد المهيري",
#     "وفاء الشامسي",
#     "سلطان النعيمي",
#     "مها الحمادي",
#     "عيسى المزروعي",
#     "نوف السويدي",
#     "طارق الشامسي",
#     "دانة المنصوري"
# ]
# df['Name']=Names
# df.to_csv('data.csv', index=False)


import pandas as pd

# Load the dataset
df = pd.read_csv("1000.csv")

# Aid scoring and labeling function
def calculate_aid_label(row):
    # Initialize score
    score = 0

    # Extract data with fallback defaults
    income = row.get('Income', 0)
    dependents = row.get('Dependents', 0)
    employment = str(row.get('Employment_Status', '')).lower()
    education = str(row.get('Education_Level', '')).lower()
    previous = str(row.get('Previous_Assistance', '')).lower()
    credit_score = row.get('Credit_Score', 0)

    # Income scoring
    if income < 5000:
        score += 30
    elif 5000 <= income <= 10000:
        score += 20
    else:
        score += 10

    # Dependents scoring
    if dependents >= 4:
        score += 20
    elif 2 <= dependents < 4:
        score += 10

    # Employment scoring
    if employment in ['عاطل عن العمل', 'عمل حر', 'دوام جزئي']:
        score += 20
    elif employment in ['متقاعد']:
        score += 15
    else:
        score += 10

    # Education scoring
    if education in ['الثانوية العامة', 'بكالوريوس']:
        score += 10
    elif education in ['ماجستير']:
        score += 5

    # Previous assistance
    if previous == 'no':
        score += 10

    # Credit score
    if credit_score < 500:
        score += 10

    # Aid amount and label based on score
    if score >= 80:
        label = "Eligible"
        aid_amount = 5000
    elif score >= 60:
        label = "Eligible"
        aid_amount = 3000
    elif score >= 40:
        label = "Eligible"
        aid_amount = 1500
    else:
        label = "Not Eligible"
        aid_amount = 0

    return pd.Series([label, score, aid_amount])

# Apply scoring to the DataFrame
df[['Financial_Aid_Label', 'Aid_Score', 'Aid_Amount']] = df.apply(calculate_aid_label, axis=1)

# Save the labeled dataset
df.to_csv("labeled_data.csv", index=False)

# Preview relevant fields
print(df[['Name', 'Income', 'Dependents', 'Employment_Status', 'Education_Level', 'Credit_Score',
          'Previous_Assistance', 'Financial_Aid_Label', 'Aid_Score', 'Aid_Amount']].head())
