import requests

url = "http://18.206.163.235:8000/"
data = {
    'title': 'Sample Title',
    'lang': 'Hindi',
    'loc': 'Sample',
    'pic': False
}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    print("Request successful. Response:", response.text)
except requests.exceptions.RequestException as e:
    print("Failed to make the request:", e)
