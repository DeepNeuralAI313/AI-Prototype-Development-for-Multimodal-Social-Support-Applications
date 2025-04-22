# import csv
# import random
# from faker import Faker

# # Use Arabic locale for Saudi Arabia
# fake = Faker('ar_SA')

# def generate_emirates_id():
#     return f"784-{random.randint(1970, 2000)}-{random.randint(1000000, 9999999)}-{random.randint(0,9)}"

# def generate_applicant():
#     employment_statuses = ['موظف', 'عاطل عن العمل', 'عمل حر', 'دوام جزئي', 'متعاقد', 'متقاعد']
#     education_levels = ['الثانوية العامة', 'بكالوريوس', 'ماجستير', 'دكتوراه']
#     regions = ['الرياض', 'جدة', 'مكة', 'الدمام', 'المدينة المنورة', 'تبوك', 'أبها', 'القصيم']

#     name = fake.name()
#     emirates_id = generate_emirates_id()
#     age = random.randint(25, 60)
#     gender = random.choice(['ذكر', 'أنثى'])
#     income = random.randint(2000, 20000)
#     dependents = random.randint(0, 6)
#     employment_status = random.choice(employment_statuses)
#     education = random.choice(education_levels)
#     previous_assistance = random.choice(['نعم', 'لا'])
#     credit_score = random.randint(500, 750)
#     region = random.choice(regions)

#     return [name, emirates_id, age, gender, income, dependents, employment_status, education, previous_assistance, credit_score, region]

# def generate_csv(filename='saudi_applicants.csv', num_records=50):
#     headers = ["الاسم", "رقم الهوية", "العمر", "الجنس", "الدخل", "المعالين", 
#                "الحالة الوظيفية", "المستوى التعليمي", "مساعدة سابقة", 
#                "درجة الائتمان", "المنطقة"]
    
#     with open(filename, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(headers)
#         for _ in range(num_records):
#             writer.writerow(generate_applicant())
    
#     print(f"{num_records} سجلًا تم حفظها في '{filename}'")

# # Run function
# generate_csv('saudi_applicants.csv', num_records=50)

# import random
# import pandas as pd

# # UAE-style Arabic names (sampled for realism)
# arabic_names = [
#     "Ahmed Al Mansoori", "Fatima Al Zaabi", "Mohammed Al Hammadi", "Aisha Al Shamsi",
#     "Hamad Al Suwaidi", "Mariam Al Nuaimi", "Khalid Al Ameri", "Noora Al Mazrouei",
#     "Saeed Al Marri", "Latifa Al Rumaithi", "Abdullah Al Ali", "Hind Al Hosani",
#     "Yousef Al Ketbi", "Salma Al Mehairi", "Omar Al Darei", "Reem Al Shamsi",
#     "Majid Al Falasi", "Layla Al Tunaiji", "Rashid Al Qubaisi", "Amna Al Shehhi",
#     "Nasser Al Kaabi", "Shaikha Al Shamsi", "Fahad Al Muhairi", "Wafa Al Shamsi",
#     "Sultan Al Nuaimi", "Maha Al Hammadi", "Essa Al Mazrouei", "Nouf Al Suwaidi",
#     "Tariq Al Shamsi", "Dana Al Mansoori"
# ]


# employment_statuses = ['موظف', 'عاطل عن العمل', 'عمل حر', 'دوام جزئي', 'متعاقد', 'متقاعد']
# education_levels = ['الثانوية العامة', 'بكالوريوس', 'ماجستير', 'دكتوراه']
# regions = ['أم القيوين', 'رأس الخيمة', 'الفجيرة', 'دبي', 'الشارقة', 'أبوظبي']

# genders = ['ذكر', 'أنثى']
# assistance = ['نعم', 'لا']

# # Function to generate Emirates ID and age
# def generate_emirates_id_and_age():
#     birth_year = random.randint(1985, 1995)
#     age = 2025 - birth_year
#     emirates_id = f"784-{birth_year}-{random.randint(1000000, 9999999)}-{random.randint(1,9)}"
#     return emirates_id, age

# # Generate data
# data = []
# for name in arabic_names[:30]:
#     emirates_id, age = generate_emirates_id_and_age()
#     gender = 'ذكر' if 'Ahmed' in name or 'Mohammed' in name or 'Hamad' in name or 'Khalid' in name or 'Saeed' in name or 'Abdullah' in name or 'Yousef' in name or 'Omar' in name or 'Majid' in name or 'Rashid' in name or 'Nasser' in name or 'Fahad' in name or 'Sultan' in name or 'Essa' in name or 'Tariq' in name else 'أنثى'
#     income = random.randint(4000, 30000)
#     row = {
#         "Name": name,
#         "Emirates_ID": emirates_id,
#         "Age": age,
#         "Gender": gender,
#         "Income": income,
#         "Dependents": random.randint(0, 5),
#         "Employment_Status": random.choice(employment_statuses),
#         "Education_Level": random.choice(education_levels),
#         "Previous_Assistance": random.choice(assistance),
#         "Credit_Score": random.randint(550, 800),
#         "Region": random.choice(regions)
#     }
#     data.append(row)

# df_uae = pd.DataFrame(data)
# df_uae.to_csv('data.csv')


# Re-import necessary modules after kernel reset
import random
import pandas as pd
from faker import Faker

fake = Faker('ar_AE')  # Arabic (United Arab Emirates) locale

# Employment and Education options
employment_statuses = ['موظف', 'عاطل عن العمل', 'عمل حر', 'دوام جزئي', 'متعاقد', 'متقاعد']
education_levels = ['الثانوية العامة', 'بكالوريوس', 'ماجستير', 'دكتوراه']
regions = ['أم القيوين', 'رأس الخيمة', 'الفجيرة', 'دبي', 'الشارقة', 'أبوظبي']

# Generate Emirates ID and calculate age
def generate_emirates_id_and_age():
    birth_year = random.randint(1985, 2000)
    id_number = f"784-{birth_year}-{random.randint(1000000, 9999999)}-{random.randint(1,9)}"
    age = 2025 - birth_year
    return id_number, age

# Arabic-style male and female names
male_names = [
    'Ahmed', 'Mohammed', 'Hamad', 'Khalid', 'Saeed', 'Abdullah', 'Yousef', 'Omar', 'Majid', 'Rashid',
    'Nasser', 'Fahad', 'Sultan', 'Essa', 'Tariq', 'Ali', 'Hassan', 'Hussein', 'Mustafa', 'Bilal',
    'Zaid', 'Ziyad', 'Ibrahim', 'Ismail', 'Abbas', 'Anas', 'Talal', 'Salman', 'Jamal', 'Ayman',
    'Basim', 'Kareem', 'Nabil', 'Faisal', 'Farid', 'Samir', 'Imran', 'Amin', 'Adnan', 'Zaki',
    'Rami', 'Mazen', 'Waleed', 'Ilyas', 'Adel', 'Yahya', 'Hashim', 'Munir', 'Othman', 'Amir',
    'Hani', 'Tamer', 'Qasim', 'Zuhair', 'Barak', 'Naeem', 'Ghassan', 'Murad', 'Samer', 'Abed',
    'Mahmoud', 'Bassam', 'Fathi', 'Hisham', 'Raed', 'Laith', 'Tawfiq', 'Rafik', 'Jabir', 'Harith',
    'Luay', 'Hilal', 'Jibril', 'Anwar', 'Sami', 'Najib', 'Arafat', 'Sadiq', 'Ridwan', 'Waleed',
    'Ihab', 'Yasir', 'Saif', 'Shaheen', 'Zaher', 'Riyad', 'Naji', 'Taha', 'Bakr', 'Marwan',
    'Alaa', 'Zubair', 'Izzuddin', 'Saad', 'Khidr', 'Rauf', 'Adeel', 'Amjad', 'Talib', 'Siraj',
    'Nizar', 'Haitham', 'Mujahid', 'Farhan', 'Junaid', 'Kamal', 'Suhail', 'Rayyan', 'Hatem',
    'Qays', 'Usama', 'Fahim', 'Zaman', 'Rashad', 'Fadil', 'Aqeeb', 'Shafiq', 'Mubarak', 'Sabir',
    'Noman', 'Khalil', 'Burhan', 'Mazhar', 'Qadir', 'Aziz', 'Safwan', 'Nawaf', 'Zubayr', 'Arif',
    'Ahsan', 'Wajid', 'Haris', 'Maaz', 'Yunus', 'Nashit', 'Rami', 'Basil', 'Abdurrahman', 'Akram',
    'Badr', 'Ghazi', 'Jaleel', 'Nuh', 'Qutb', 'Salah', 'Umar', 'Wahid', 'Zafar', 'Hamza',
    'Irfan', 'Naif', 'Tameem', 'Zaeem', 'Zayyan', 'Taj', 'Kazi', 'Obaid', 'Shihab', 'Zain',
    'Shakir', 'Ammar', 'Ashraf', 'Dawood', 'Fawwaz', 'Imad', 'Jawad', 'Khayyam', 'Nashwan',
    'Rafaan', 'Shamil', 'Thabit', 'Wael', 'Yameen', 'Zidan', 'Aban', 'Aariz', 'Bashir', 'Ehsan',
    'Ghalib', 'Hilmi', 'Iskandar', 'Jamaluddin', 'Kaamil', 'Latif', 'Mahdi', 'Naseem', 'Qasim',
    'Razi', 'Sahib', 'Tamim', 'Ubaid', 'Wali', 'Yahyaa', 'Zeeshan', 'Abdulaziz', 'Azlan', 'Baqar',
    'Daniyal', 'Elham', 'Fazal', 'Gibran', 'Hamid', 'Ilham', 'Junaid', 'Kareem', 'Lutfi', 'Mazin',
    'Nashit', 'Omar', 'Pervaiz', 'Qais', 'Rameez', 'Shan', 'Talha', 'Usman', 'Vaseem', 'Waseem',
    'Xavier', 'Yasir', 'Ziyad', 'Adham', 'Ayman', 'Baraa', 'Daoud', 'Elias', 'Faris', 'Ghufran',
    'Hisham', 'Ishaq', 'Jibreel', 'Khaled', 'Luqman', 'Mujtaba', 'Naveed', 'Othman', 'Parvez',
    'Qamar', 'Rauf', 'Sulaiman', 'Tariq', 'Uthman', 'Vahid', 'Wajahat', 'Yahya', 'Zakariya',
    'Abdurrahim', 'Amr', 'Bari', 'Dani', 'Emad', 'Fadi', 'Ghaith', 'Haroon', 'Ibrahim', 'Jaleel',
    'Karam', 'Labeeb', 'Mahboob', 'Nauman', 'Owais', 'Qudamah', 'Ruhullah', 'Shaaban', 'Tameem',
    'Usayd', 'Wahid', 'Yaqoob', 'Zarif', 'Abdulrahman', 'Ahmad', 'Basharat', 'Dilshad', 'Ebrahim',
    'Furkan', 'Ghazali', 'Habib', 'Ibtisam', 'Jamshid', 'Kamran', 'Luqmaan', 'Mansoor', 'Najeeb',
    'Omar', 'Qamaruddin', 'Ramees', 'Sharif', 'Tayyab', 'Ubadah', 'Waliullah', 'Yusuf', 'Zakir',
    'Adil', 'Azhar', 'Bilqis', 'Dhiya', 'Emran', 'Fouad', 'Gulzar', 'Hammad', 'Ihsan', 'Junaid',
    'Khalfan', 'Latif', 'Munawwar', 'Nashwan', 'Omar', 'Qaisar', 'Raziq', 'Shahrukh', 'Taqi',
    'Umar', 'Waqar', 'Yunus', 'Zubair', 'Abid', 'Ashfaq', 'Baari', 'Dani', 'Faiz', 'Gamal',
    'Hashir', 'Idris', 'Jibraeel', 'Khan', 'Labeed', 'Momin', 'Naqeeb', 'Owais', 'Parwez', 'Qasim',
    'Riyaz', 'Sameer', 'Tahir', 'Umair', 'Wajid', 'Yasir', 'Zain', 'Abdul', 'Azaan', 'Burhanuddin',
    'Dhiyauddin', 'Fayaz', 'Ghiyas', 'Husam', 'Ismail', 'Jibran', 'Khubaib', 'Labeeb', 'Marwan',
    'Noman', 'Osama', 'Qutaibah', 'Ridha', 'Salih', 'Taher', 'Usaid', 'Wahaj', 'Yameen', 'Zeeshan'
]
female_names = [
    'Fatima', 'Aisha', 'Mariam', 'Noora', 'Latifa', 'Hind', 'Salma', 'Reem', 'Layla', 'Amna',
    'Shaikha', 'Wafa', 'Maha', 'Nouf', 'Dana', 'Zainab', 'Rania', 'Yasmin', 'Sumaya', 'Lubna',
    'Khadija', 'Sara', 'Huda', 'Alya', 'Nadia', 'Ruqayya', 'Asma', 'Najwa', 'Samira', 'Hiba',
    'Jamila', 'Lamia', 'Abeer', 'Iman', 'Nour', 'Rana', 'Fouzia', 'Afnan', 'Tasneem', 'Mona',
    'Najah', 'Farah', 'Sahar', 'Afra', 'Shaima', 'Nawal', 'Bushra', 'Souad', 'Nisreen', 'Basma',
    'Ghada', 'Maysoon', 'Thuraya', 'Amani', 'Rawan', 'Dina', 'Rim', 'Nada', 'Rasha', 'Sawsan',
    'Lina', 'Shatha', 'Wijdan', 'Nadine', 'Hanan', 'Tala', 'Marwa', 'Manal', 'Widad', 'Jumana',
    'Haifa', 'Azza', 'Doaa', 'Anoud', 'Noura', 'Zahra', 'Mariam', 'Kawthar', 'Ahlam', 'Haneen',
    'Wardah', 'Nihal', 'Balqees', 'Zain', 'Rabab', 'Mayar', 'Maysaa', 'Lujain', 'Ritaj', 'Thanaa',
    'Ikram', 'Sundus', 'Fatin', 'Malak', 'Nahla', 'Husna', 'Ibtisam', 'Muna', 'Wasan', 'Rawya',
    'Ilham', 'Majida', 'Duaa', 'Ayah', 'Sahar', 'Alya', 'Rahma', 'Narmeen', 'Arwa', 'Yumna',
    'Safa', 'Anisa', 'Madiha', 'Kenza', 'Ruwi', 'Shahed', 'Aseel', 'Bayan', 'Hoor', 'Thuraya',
    'Rowan', 'Rola', 'Layan', 'Shahd', 'Seham', 'Zubaida', 'Nujoud', 'Nahed', 'Rihab', 'Taqwa',
    'Ghada', 'Areej', 'Narmeen', 'Lubabah', 'Jenan', 'Tahani', 'Zayna', 'Nourah', 'Afrah', 'Nihal',
    'Jamila', 'Kifah', 'Zahira', 'Haleema', 'Aaliyah', 'Najla', 'Sireen', 'Asra', 'Roqaya',
    'Khadra', 'Samar', 'Haleemah', 'Ihsan', 'Jawaher', 'Zahraa', 'Batoul', 'Razan', 'Arij', 'Shams',
    'Salwa', 'Feryal', 'Shatha', 'May', 'Ruba', 'Ayat', 'Shaista', 'Nashwa', 'Ranya', 'Wurood',
    'Riyam', 'Noor', 'Tuba', 'Hanin', 'Imane', 'Nasma', 'Zainah', 'Hind', 'Sana', 'Sirine', 'Faiza',
    'Maisa', 'Rimsha', 'Ward', 'Jamela', 'Maysa', 'Misk', 'Bushra', 'Kalthoum', 'Soumaya',
    'Dalal', 'Hooria', 'Nimat', 'Raya', 'Tamara', 'Maram', 'Lama', 'Muneera', 'Najd', 'Zina',
    'Yusra', 'Anhar', 'Basima', 'Alaa', 'Salima', 'Samarah', 'Naela', 'Raziya', 'Suhaila',
    'Tahira', 'Ghazal', 'Hooriyah', 'Khawla', 'Lubna', 'Madinah', 'Naaz', 'Salsabeel', 'Samah',
    'Talaah', 'Yamama', 'Rihana', 'Asiyah', 'Zubaidah', 'Najiyya', 'Naila', 'Samiha', 'Sawsan',
    'Taybah', 'Wardeh', 'Yumna', 'Rameen', 'Aida', 'Haneefa', 'Juwairiya', 'Leen', 'Marjan',
    'Muzna', 'Nazneen', 'Rafiah', 'Shaima', 'Wajeeha', 'Zarifa', 'Amara', 'Bariyah', 'Daima',
    'Eman', 'Fahima', 'Ghaliyah', 'Hira', 'Iqra', 'Janna', 'Kainat', 'Lulwa', 'Meher', 'Nabihah',
    'Olfat', 'Qamar', 'Rafia', 'Saba', 'Tabassum', 'Ulfah', 'Walaa', 'Yusrah', 'Zohra', 'Azhar',
    'Amena', 'Barirah', 'Dareen', 'Elham', 'Farzana', 'Ghazala', 'Hamideh', 'Inaaya', 'Jewel',
    'Kiran', 'Laila', 'Mahira', 'Nahla', 'Omnia', 'Parveen', 'Qistina', 'Rabia', 'Sabreen', 'Tazeen',
    'Umaiza', 'Wania', 'Zeenat', 'Almas', 'Aqeela', 'Benazir', 'Chandni', 'Daniya', 'Eimaan',
    'Fadilah', 'Gulzar', 'Halimah', 'Ifrah', 'Javaria', 'Kubra', 'Liyana', 'Mahnoor', 'Naazneen',
    'Omaira', 'Pakeeza', 'Qandeel', 'Rimsha', 'Sabeen', 'Tamanna', 'Unaysah', 'Warda', 'Zunaira',
    'Alaia', 'Aysha', 'Badriyah', 'Camilia', 'Delilah', 'Esma', 'Fariha', 'Gul', 'Hoorain',
    'Imaan', 'Juveria', 'Kamila', 'Laiba', 'Maisha', 'Nimra', 'Omera', 'Perveen', 'Qamarunnisa',
    'Ranya', 'Samreen', 'Tameemah', 'Urwah', 'Wajiha', 'Zainab', 'Amal', 'Bushra', 'Dania', 'Ebtisam',
    'Farida', 'Ghadir', 'Habiba', 'Inaya', 'Jawaher', 'Khalida', 'Lamees', 'Mawadda', 'Nawal',
    'Ola', 'Rabiyah', 'Sanae', 'Tamia', 'Umniah', 'Wesam', 'Yumna', 'Zulaikha', 'Afrah', 'Buthaina',
    'Duha', 'Ehsan', 'Fareeda', 'Ghadeer', 'Haneen', 'Ibtihal', 'Jannah', 'Karima', 'Lobna',
    'Mawiya', 'Nasima', 'Ohood', 'Rim', 'Sondos', 'Thurya', 'Uzma', 'Wissal', 'Yusur', 'Zawiya',
    'Anoud', 'Baraka', 'Duaa', 'Esraa', 'Fatinah', 'Ghaziyah', 'Husniyah', 'Izdihar', 'Jamla',
    'Kawtar', 'Layanah', 'Mahasin', 'Nouriya', 'Rabab', 'Sabeha', 'Taima', 'Umayma', 'Wardiyah',
    'Yamnah', 'Zahrah'
]
last_names = ['Al Mansoori', 'Al Zaabi', 'Al Hammadi', 'Al Shamsi', 'Al Suwaidi', 'Al Nuaimi', 'Al Ameri', 'Al Mazrouei', 'Al Marri', 'Al Rumaithi', 'Al Ali', 'Al Hosani', 'Al Ketbi', 'Al Mehairi', 'Al Falasi', 'Al Tunaiji', 'Al Qubaisi', 'Al Kaabi', 'Al Muhairi', 'Al Shehhi']

# Generate dataset
data = []
for _ in range(1000):
    gender_label = random.choice(['male', 'female'])
    if gender_label == 'male':
        first_name = random.choice(male_names)
        gender = 'ذكر'
    else:
        first_name = random.choice(female_names)
        gender = 'أنثى'
    full_name = f"{first_name} {random.choice(last_names)}"
    eid, age = generate_emirates_id_and_age()
    income = random.randint(5000, 30000)
    dependents = random.randint(0, 5)
    employment = random.choice(employment_statuses)
    education = random.choice(education_levels)
    prev_assistance = random.choice(['نعم', 'لا'])
    credit_score = random.randint(550, 800)
    region = random.choice(regions)

    data.append([
        full_name, eid, age, gender, income, dependents,
        employment, education, prev_assistance, credit_score, region
    ])

columns = [
    "Name", "Emirates_ID", "Age", "Gender", "Income", "Dependents",
    "Employment_Status", "Education_Level", "Previous_Assistance",
    "Credit_Score", "Region"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv('1000.csv')
