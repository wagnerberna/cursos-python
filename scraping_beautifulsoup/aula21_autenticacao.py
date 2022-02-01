from bs4 import BeautifulSoup
import requests

url = 'http://httpbin.org/basic-auth/user/passwd'

# erro sem enviar dados de autenticação
req = requests.get(url)
print(req.status_code)

# req com sucesso
req = requests.get(url, auth=('user', 'passwd'))
print(req.status_code)
soup = BeautifulSoup(req.text, 'lxml')
print(soup)
print('-----')
print(soup.p)
print('-----')
print(soup.p.get_text())
