from storyapp.gemini.gemini import *
from storyapp.image_gen import *
from storyapp.gemini.geminivision import *
import pandas as pd
import time 
import cv2
from PIL import Image
from aws import *
import os
from storyapp.data_to_video import *


def main_story(title,lang,loc,pic):
    if pic:
        download_data_from_s3(loc)
    try:
        story1=g_model(f"act as professional story writter with 100 year experience. write an impressive story. its must be correlated and in sequency. the story description is = {title},story language ={lang}. negative prompts= low quality text, boring, not looks story, not attractive. ")
    except:
        print("issue with story generation")
        pass

    folder_names = [f'{loc}/audio', f'{loc}/doc', f'{loc}/image', f'{loc}/gif',f'{loc}/video',f'{loc}/raw_images']

    try:
        for folder_name in folder_names:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name, exist_ok=True)
                print(f'Folder "{folder_name}" created successfully.')
            else:
                print(f'Folder "{folder_name}" already exists.')
    except Exception as e:
        print("issue with folders creation")
        print(f"An error occurred: {e}")
    
    split_essay_into_csv(story1,loc)
    
    
    promp_gen(lang,loc,pic)
    try:
        create_video(loc)
    except:
        print("issue with video creation" )
        pass

    try:
        upload_data_to_s3(loc)
    except:
        print("issue with uploading data")
        pass

    try:
        time.sleep(10)
        #sdelete_folder(loc)
    except:
        print("issue with deleting folders")
        pass


    return "done"

def split_essay_into_csv(essay_text,loc):
    paragraphs = essay_text.split('\n\n')
    df = pd.DataFrame(paragraphs, columns=['Paragraph'])
    df.to_csv(f"{loc}/doc/paragraphs.csv", index=False)
    #upload_data_to_s3(f"{loc}/doc/paragraphs.csv")



def promp_gen(lang,loc,pic):
    data=pd.read_csv(f"{loc}/doc/paragraphs.csv")
    i=0
    image_paths=fetch_image_paths(loc)
    for i in range(len(data)):
        para=data["Paragraph"][i]
        text_to_speech(para,lang,f"{loc}/audio/{i}.mp3")
        #upload_data_to_s3(f"{loc}/audio/{i}.mp3")
        try:
            if pic:
                if image_paths[i]:
                    img=cv2.imread(image_paths[i])
                    image_pro=gv_model(f"i have an image and text. based on both image and text you have to create an image generation prompt which must reflect both things. this is an image = {img} and this is text=f{para}. generate an best prompt and details prompts")
            else:
                image_pro=g_model(f"convert given text into image generation prompet, prompet must be accurate and reflect the text. image must be hight resolution and landscape. text=f{para}. generate an best prompt and details prompts. focuse must be on charector ")
        except:
            pass
        image_gen(loc,image_pro+".high resultion image. negative_prompt = nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]",i)
    return image_pro
#story=main_story("the poor young boy fall in love","English (US)","raheem/034")


import os

def fetch_image_paths(folder_name):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_paths = []

    # Traverse the directory
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            # Check if the file has a supported image extension
            if os.path.splitext(file)[1].lower() in image_extensions:
                # Construct the full file path
                file_path = os.path.join(root, file)
                # Add the file path to the list
                image_paths.append(file_path)
                

    return image_paths

import shutil

def delete_folder(folder_path):
    try:
        # Delete the folder and its contents
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' deleted successfully.")
        return True
    except Exception as e:
        print(f"An error occurred while deleting folder '{folder_path}': {e}")
        return False





