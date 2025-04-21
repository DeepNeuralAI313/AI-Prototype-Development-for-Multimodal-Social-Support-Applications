import cv2
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import numpy as np


def add_text(cv_img,emirates_ID,name_in_arabic,name_in_english):
    
    # Convert to RGB (for PIL)
    cv_img_rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(cv_img_rgb)
    draw = ImageDraw.Draw(img_pil)

    # Load Arabic font (make sure you have a proper Arabic font file)
    font_path = 'data colaction & preprocessing/Amiri/Amiri-Regular.ttf'
    font = ImageFont.truetype(font_path, 23)

    # Prepare Arabic text
    # name_in_english=translate_name(arabic_text)
    reshaped_text = arabic_reshaper.reshape(name_in_arabic)
    bidi_text = get_display(reshaped_text)


    # Prepare Arabic text
    arabic_text = 'الجنسية : الإمارات   العربية  المتحدة'
    reshaped_text = arabic_reshaper.reshape(arabic_text)
    bidi_text2 = get_display(reshaped_text)


    # Draw the Arabic text
    draw.text((178, 287), name_in_english, font=font,stroke_width=1, fill=(50, 50, 50))
    draw.text((400, 237), bidi_text, font=font,stroke_width=1, fill=(50, 50, 50))
    draw.text((243, 335),bidi_text2 , font=font,stroke_width=1, fill=(50, 50, 50))
    # Draw English text with PIL too (or use cv2.putText if you prefer)
    draw.text((300, 165),emirates_ID,stroke_width=1,   font=ImageFont.truetype(font_path, 18), fill=(50, 50, 50))
    draw.text((178, 414), 'Note - This is a dummy record generated for experiment purpose',stroke_width=1,   font=ImageFont.truetype(font_path, 18), fill=(50, 50, 50))


    # Convert back to BGR for OpenCV
    final_img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    return final_img
def addd_small_image(image,new_image):
    
    # Define region where the image will be inserted (ensure it's in bounds)
    y1, y2 = 118, 183
    x1, x2 = 700, 761

    # Resize new image to fit into the target area
    target_height = y2 - y1
    target_width = x2 - x1
    resized_image = cv2.resize(new_image, (target_width, target_height))

    resized_image=cv2.cvtColor(resized_image,cv2.COLOR_RGB2GRAY)
    gray_bgr_image = cv2.cvtColor(resized_image, cv2.COLOR_GRAY2BGR)

    # Replace the region in the original image
    image[y1:y2, x1:x2] = gray_bgr_image
    return image

def add_image(image,new_image):
    # Define region where the image will be inserted (ensure it's in bounds)
    y1, y2 = 210, image.shape[0] - 20
    x1, x2 = 560, image.shape[1] - 25

    # Resize new image to fit into the target area
    target_height = y2 - y1
    target_width = x2 - x1
    resized_image = cv2.resize(new_image, (target_width, target_height))

    # Replace the region in the original image
    image[y1:y2, x1:x2] = resized_image
    return image 



if __name__=="__main__":
    import os
    import pandas as pd
    try:
        os.mkdir('ID')
    except:
        pass
    # Load the base ID card image

    all_man_images=next(os.walk('data colaction & preprocessing/user_man_female_identify_photo/user_man_female_identify_photo/Man'))[2]
    all_female_images=next(os.walk('data colaction & preprocessing/user_man_female_identify_photo/user_man_female_identify_photo/female'))[2]
    # print(all_female_images)
    # Load the new photo to insert

    m_status=0
    f_status=0
    df=pd.read_csv('data.csv')

    for _,i in df.iterrows():
        image = cv2.imread('data colaction & preprocessing/dummy_id_card-Photoroom.jpg')

        name = i['Name']
        name_in_english = i['name_in_english']
        emirates_id = i['Emirates_ID']
        gender = i['Gender']

        if gender == 'ذكر':
            file_name=all_man_images[m_status]
            print(file_name)
            new_image = cv2.imread(f'data colaction & preprocessing/user_man_female_identify_photo/user_man_female_identify_photo/Man/{file_name}')
            m_status+=1

            image=add_image(image,new_image)
            image=addd_small_image(image,new_image)
            image=add_text(image,emirates_id,name,name_in_english)
                # Display the final image

            cv2.imwrite(f'ID/{name_in_english}.jpg',image)
            # cv2.imshow('ID Card with New Photo', image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

        else:
            file_name=all_female_images[f_status]
            new_image = cv2.imread(f'data colaction & preprocessing/user_man_female_identify_photo/user_man_female_identify_photo/female/{file_name}')
            f_status+=1

            image=add_image(image,new_image)
            image=addd_small_image(image,new_image)
            image=add_text(image,emirates_id,name,name_in_english)
            cv2.imwrite(f'ID/{name_in_english}.jpg',image)
            # cv2.imshow('ID Card with New Photo', image)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()


    

