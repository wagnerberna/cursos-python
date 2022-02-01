from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

print("---Navegando entre filhos----")
print(soup.body.contents)
print(type(soup.body.contents))
print(len(soup.body.contents))
print(soup.body.contents[0])
print(soup.body.contents[2])
print(soup.body.contents[2].a['href'])

print(soup.body.contents[2].get_text())
# ou
print(soup.body.contents[2].string)

print("---FOR para pegar os Filhos----")
for child in soup.body.contents:
    if child.name == 'li':
        print(child)
        print(child.a.get('href'))
        print(child.get_text())
