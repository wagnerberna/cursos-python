from bs4 import BeautifulSoup
import requests

# Erro de conexão end. não existe
try:
    endpoint = 'https://sample-university-site.herokuappKKKKKKK.com/approvals/1'
    req = requests.get(endpoint)
    # cria instância do BeautifulSoup
    soup = BeautifulSoup(req.text, 'lxml')

    print(req.status_code)

except requests.exceptions.ConnectionError as e:
    print(str(e))

print('--------')
# timeout error
try:
    endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
    req = requests.get(endpoint, timeout=0.3)
    # cria instância do BeautifulSoup
    soup = BeautifulSoup(req.text, 'lxml')

    print(req.status_code)

except requests.exceptions.Timeout as e:
    print(str(e))


print('--------')
# Erro URL inválida
try:
    endpoint = '.com'
    req = requests.get(endpoint, timeout=0.3)
    # cria instância do BeautifulSoup
    soup = BeautifulSoup(req.text, 'lxml')

    print(req.status_code)

except requests.exceptions.RequestException as e:
    print(str(e))