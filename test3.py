import requests



res = requests.post('http://60.204.173.235:5001/test')
print(res.text)