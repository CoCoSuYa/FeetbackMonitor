import requests

data = {
  "text": {
    "content": "你好"
  }
}

res = requests.get('http://60.204.173.235:5001/handle-request', json=data)
print(res.text)