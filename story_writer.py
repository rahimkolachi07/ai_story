from gemini.gemini import *
from image_gen import *
from gemini.geminivision import *
import pandas as pd
import time 
import cv2
from PIL import Image
from aws import *
import os
from data_to_video import *


def main_story(title,lang,loc):
    story1=g_model(f"act as professional story writter with 100 year experience. write an impressive story. its must be correlated and in sequency. the story title is = {title},story language ={lang}. negative prompts= low quality text, boring, not looks story, not attractive. ")

    folder_names = [f'{loc}/audio', f'{loc}/doc', f'{loc}/image', f'{loc}/gif',f'{loc}/video']

    try:
        for folder_name in folder_names:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name, exist_ok=True)
                print(f'Folder "{folder_name}" created successfully.')
            else:
                print(f'Folder "{folder_name}" already exists.')
    except Exception as e:
        print(f"An error occurred: {e}")
    
    split_essay_into_csv(story1,loc)
    promp_gen(lang,loc)
    create_video(loc)
    upload_data_to_s3(f'{loc}/video/output_video.mp4',object_name=None)


    return story1

def split_essay_into_csv(essay_text,loc):
    paragraphs = essay_text.split('\n\n')
    df = pd.DataFrame(paragraphs, columns=['Paragraph'])
    df.to_csv(f"{loc}/doc/paragraphs.csv", index=False)
    upload_data_to_s3(f"{loc}/doc/paragraphs.csv",object_name=None)



def promp_gen(lang,loc):
    data=pd.read_csv(f"{loc}/doc/paragraphs.csv")
    i=0
    for i in range(len(data)):
        para=data["Paragraph"][i]
        text_to_speech(para,lang,f"{loc}/audio/{i}.mp3")
        upload_data_to_s3(f"{loc}/audio/{i}.mp3",object_name=None)
        
        image_pro=g_model(f"convert given text into image generation prompet, prompet must be accurate and reflect the text. image must be hight resolution and landscape. text=f{para}.")
        print(image_pro)
        image_gen(loc,image_pro+".high resultion image. negative_prompt = nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]",i)
    return image_pro
story=main_story("the poor young boy fall in love","English (US)","raheem/034")




