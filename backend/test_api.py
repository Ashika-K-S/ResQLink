import urllib.request
import json

url = 'http://127.0.0.1:8000/api/token/'
data = json.dumps({"username":"ashikaksuresh@gmail.com","password":"password123"}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

try:
    response = urllib.request.urlopen(req)
    print("Success:")
    print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
