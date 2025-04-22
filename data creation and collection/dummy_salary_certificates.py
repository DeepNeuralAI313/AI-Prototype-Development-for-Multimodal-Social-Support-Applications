from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import arabic_reshaper
from bidi.algorithm import get_display
import os
import pandas as pd
import numpy as np
# Register Arabic font (make sure the .ttf file exists in your project folder)
font_path = 'data colaction & preprocessing/Amiri/Amiri-Regular.ttf'
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont('Arabic', font_path))
else:
    raise FileNotFoundError(f"Font not found at: {font_path}")

def reshape_rtl(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text


def salary_certificate_arabic(
    filename='salary_cert_detailed.pdf',
    name='محمد العتيبي',
    emirates_id='784-1987-1234567-1',
    age='35',
    gender='ذكر',
    income='15000',
    employment_status='دوام كامل',
    region='الرياض',
    employer='شركة الرياض للتجارة',
    logo_path='data colaction & preprocessing/company logo/download.jpg'
):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    if employer!="UAE Government":
        # Add the logo at the top of the page (adjust position and size as needed)
        if os.path.exists(logo_path):
            logo_width = 100  # Adjust width as necessary
            logo_height = 60  # Adjust height as necessary
            c.drawImage(logo_path, 40, height - 70, logo_width, logo_height)
        else:
            raise FileNotFoundError(f"Logo not found at: {logo_path}")
    
    c.setFont("Arabic", 16)
    c.drawRightString(width / 2 + 100, height - 80, reshape_rtl("شهادة راتب وتفاصيل الموظف"))
    c.drawRightString(180, height - 110, reshape_rtl("التاريخ: 2025-04-15"))

    c.setFont("Arabic", 12)
    y = height - 130

    intro = f"""
    إلى من يهمه الأمر،
    
    نفيدكم نحن {employer} بأن المعلومات التالية تخص أحد موظفينا ونؤكد على صحتها.
    تم إصدار هذه الشهادة بطلب من الموظف لغرض التقديم لأي جهة تتطلب إثبات دخل أو حالة توظيف.
    """

    for line in intro.strip().split("\n"):
        c.drawRightString(width - 80, y, reshape_rtl(line.strip()))
        y -= 25

    y -= 5  # space before main details
    details = f"""
    الاسم الكامل: {name}
    العمر: {age} سنة
    الجنس: {gender}
    الحالة الوظيفية: {employment_status}
    الدخل الشهري: {income} AED
    المنطقة: {region}
    """

    for line in details.strip().split("\n"):
        c.drawRightString(width - 80, y, reshape_rtl(line.strip()))
        y -= 25

    # Footer
    c.drawRightString(150, y - 10, reshape_rtl("مع خالص التحية،"))
    c.drawRightString(150, y - 30, reshape_rtl(employer))

    c.save()
    print(f"📄 PDF saved as: {filename}")


def salary_certificate_english(
    filename='salary_cert_detailed.pdf',
    name='محمد العتيبي',  # Arabic Name
    emirates_id='784-1987-1234567-1',
    age='35',
    gender='ذكر',  # Arabic for Male
    income='15000',
    employment_status='دوام كامل',  # Arabic for Full-time
    region='الرياض',  # Arabic for Riyadh
    employer='شركة الرياض للتجارة',  # Arabic Employer
    logo_path='data colaction & preprocessing/company logo/download.jpg'
):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    if employer!="UAE Government":
        # Add the logo at the top of the page (adjust position and size as needed)
        if os.path.exists(logo_path):
            logo_width = 100  # Adjust width as necessary
            logo_height = 60  # Adjust height as necessary
            c.drawImage(logo_path, 40, height - 70, logo_width, logo_height)
        else:
            raise FileNotFoundError(f"Logo not found at: {logo_path}")
    # Title in English
    c.setFont("Arabic", 16)
    c.drawRightString(width /2 + 100, height - 80, reshape_rtl("Salary Certificate and Employee Details"))

    # Date in English
    c.setFont("Arabic", 12)
    c.drawRightString(width - 100, height - 110, reshape_rtl("Date: 2025-04-15"))

    c.setFont("Arabic", 12)
    y = height - 130

    # Introduction in English
    intro = f"""
    To Whom It May Concern,
             
    """
    


    for line in intro.strip().split("\n"):
        c.drawRightString(width-80, y, reshape_rtl(line.strip()))
        y -= 25

    c.drawRightString(width - 100, y - 20, reshape_rtl(f"We, {employer}, hereby confirm that the following information pertains to one of our"))
    c.drawRightString(width - 105, y - 40, reshape_rtl("employees and we affirm its accuracy. This certificate is issued upon the employee's request"))
    c.drawRightString(width - 150, y - 60, reshape_rtl("for submission to any entity that requires proof of income or employment status. "))
    y -= 120  # space before main details

    # Employee details in English with Arabic values
    details = f"""
    Full Name: {name}
    Age: {age} years
    Gender: {gender}
    Employment Status: {employment_status}
    Monthly Income: {income} AED
    Region: {region}
    """

    for line in details.strip().split("\n"):
        c.drawRightString(width - 80, y, reshape_rtl(line.strip()))
        y -= 25

    # Footer in Arabic
    c.drawRightString(150, y - 10, reshape_rtl("With best regards,"))
    c.drawRightString(150, y - 30, reshape_rtl(employer))

    c.save()
    print(f"📄 PDF saved as: {filename}")

# Generate the PDF


if __name__ == "__main__":
    try:
        os.mkdir('salary_certificate')
    except:
        pass
    df=pd.read_csv('data.csv')
    company_name=['ADNOC','Dragon Oil','UAE Government']
    for _,i in df.iterrows():
        # Name,Emirates_ID,Age,Gender,Income,Dependents,Employment_Status,Education_Level,Previous_Assistance,Credit_Score,Region
        name = i['Name']
        name_in_english=i['name_in_english']
        emirates_id = i['Emirates_ID']
        age = i['Age']
        gender = i['Gender']
        employment_status = i['Employment_Status']
        income = i['Income']
        region = i['Region']
        filename = f"salary_certificate/{name}.pdf"
        random_certificate_type= np.random.randint(0,2,1)[0]
        employer=company_name[np.random.randint(0,3,1)[0]]
        image_path='data colaction & preprocessing/company logo/'+employer+'.jpg'
        if random_certificate_type==0:
            salary_certificate_english(filename=filename,name=name_in_english,emirates_id= emirates_id,age= age, gender=gender,employment_status= employment_status,income= income,region= region,employer=employer,logo_path=image_path)
        else:
            salary_certificate_arabic(filename=filename,name=name,emirates_id= emirates_id,age= age, gender=gender,employment_status= employment_status,income= income,region= region,employer=employer,logo_path=image_path)


#   filename='salary_cert_detailed.pdf',
#     name='محمد العتيبي',
#     emirates_id='784-1987-1234567-1',
#     age='35',
#     gender='ذكر',
#     income='15000',
#     employment_status='دوام كامل',
#     region='الرياض',
#     employer='شركة الرياض للتجارة'
# ):

# filename='salary_cert_detailed.pdf',
#     name='محمد العتيبي',  # Arabic Name
#     emirates_id='784-1987-1234567-1',
#     age='35',
#     gender='ذكر',  # Arabic for Male
#     income='15000',
#     employment_status='دوام كامل',  # Arabic for Full-time
#     region='الرياض',  # Arabic for Riyadh
#     employer='شركة الرياض للتجارة',  # Arabic Employer
#     logo_path='data colaction & preprocessing/company logo/download.jpg'