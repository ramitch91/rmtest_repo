import requests

r = requests.get("http://github.com")
print(r.status_code)
print(r.ok)
