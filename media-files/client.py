import requests

url = "http://localhost:5000/test-file"

file = {"media": open('dog.jpg', 'rb')}

r = requests.post(url, files=file)

print(r)