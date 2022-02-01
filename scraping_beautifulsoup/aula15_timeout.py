from bs4 import BeautifulSoup
import requests

# timeout tempo de espera pela req. em segundos
# tempo param. (req., leitura)
# (None) infinito / mto baixo erro
endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint, timeout=(0.5,3))
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

print(req)