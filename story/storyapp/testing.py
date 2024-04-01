import requests

# Define the URL of your API endpoint
url = 'http://18.206.163.235:8000/generate_story/'

# Define parameters for your request
params = {
    'title': 'king is the king',
    'lang': 'Hindi',
    'loc': 'Yoo',
    'pic': False
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
