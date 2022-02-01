from bs4 import BeautifulSoup
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals1111/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

print(req.status_code)
if req.status_code == requests.codes.ok:
    print('Sem erros')
if req.status_code != requests.codes.ok:
    print('Erro na requisição')

# capturar cabeçalho de resposta:
print(req.headers)

# capturar cookie
print(req.headers['Set-Cookie'])