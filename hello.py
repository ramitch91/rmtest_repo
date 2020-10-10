import requests
import sys

print(sys.executable)

r = requests.get("http://github.com")
print(r.status_code)
print(r.ok)
