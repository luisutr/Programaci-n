import requests

r = requests.get('http://httpbin.org')
if r.status_code == 200:
    print("ok")
    codigo = r.text
    print(codigo)
else:
    print("Web no furula")