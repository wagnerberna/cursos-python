from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

print("---para pegar os Filhos Diretos----")
# Pega os filhos diretos:
print(list(soup.children))
print("---para pegar os Filhos descendentes----")
# Pega os filhos indiretos descendentes dos filhos:
print(list(soup.descendants))

print("---Verificar se os descendentes são uma string de navegação----")
for tag in soup.descendants:
    if isinstance(tag, NavigableString):
        print(tag)
    else:
        print(tag.name)

print("---Verificar se os descendentes são uma tag----")
for tag in soup.descendants:
    if isinstance(tag, Tag):
        print(tag)
