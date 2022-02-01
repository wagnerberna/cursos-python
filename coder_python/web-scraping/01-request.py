import requests

print(requests.get("https://www.betrybe.com/"))
# Response[200]

req = requests.get("https://www.betrybe.com/")
print(req.status_code)
# 200
print(req.headers)

print(req.headers["content-Type"])
# text / html

print(req.text)
# retorna todo HTML puro
