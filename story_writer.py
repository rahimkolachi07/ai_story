from gemini.gemini import *
def main_story(title,category,lang):
    story1=g_model(f"write an story title is = {title}, category is ={category}, language ={lang}.  word count must be greater then 2000 .start with introduction with cheractors name then body then interval then last part of the story and dont mention any headings,. negative prompts= low quality text, boring, not looks story. ")
    return story1
story1=main_story("the begning of the young love","fantasy","english")
print(story1)
essay_text=story1


import pandas as pd

def split_essay_into_csv(essay_text, loc):
    paragraphs = essay_text.split('\n\n')
    df = pd.DataFrame(paragraphs, columns=['Paragraph'])
    df.to_csv(f"{loc}/paragraphs.csv", index=False)

def promp_gen(loc):
    data=pd.read_csv(f"{loc}/paragraphs.csv")
    for i,para in enumerate(data):
        image_pro=g_model(f"convert given text into one image generation prompet. text=f{para} ")
    return image_pro
#prompt=promp_gen(story1)


