import requests


url = 'http://127.0.0.1:5000/uploadfile'
file = open("1.jpeg", 'rb')
files = {'file': ('../new_name.jpg', file)}
response = requests.post(url, files=files)
file.close()