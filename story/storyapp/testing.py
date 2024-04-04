import requests
def req_test():
    # Define the URL of your API endpoint
    url = 'http://18.206.163.235:8000/generate_story/'

    # Define parameters for your request
    params = {
        'title': 'there is a boy who is the worror of the darknes and missing chiled of the king. write long story',
        'lang': 'Hindi',
        'loc': 'hammad8OC2wNW',
        'pic': True
    }

    # Make a GET request to the API endpoint
    response = requests.get(url, params=params)

    # Check the response status code
    if response.status_code == 200:
        # If the request was successful, print the result
        data = response.json()
        print("Result:", data['result'])
    else:
        # If there was an error, print the error message
        print("Error:", response.text)
from gemini.geminivision import *
from PIL import Image
import cv2

# Open an image file
image_path = "9.png" 
# Provide the path to your image
img = Image.open(image_path)


text=gv_model(f"i need text as output. Using both the image and text provided, your task is to craft a prompt for generating an image that reflects the essence of both. The accompanying text reads as follows: work is the best. Make sure the prompt captures the essence of both the text and image in a cohesive and impactful manner. return only text. i just need text format",img)
print(text)