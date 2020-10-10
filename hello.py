import requests

r = requests.get("http://twitter.com")
print(r.status_code)
print(r.ok)