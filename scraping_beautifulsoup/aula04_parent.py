from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')
tag_h1 = soup.h1

print("---Acessando os Pais---")
print(tag_h1)
print(tag_h1.parent.name)

print("---Acessando o Pai do pai -avô---")
print(tag_h1.parent.parent.name)
