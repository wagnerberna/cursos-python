from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

print("----soup---")
print(soup)
print("----prettify---")
print(soup.prettify())
print("----get_text---")
print(soup.get_text())
print("----tag---")
tag = soup.h1
print(f"Nome da TAG: {tag.name}")
# mostrar atributos da tag
print(tag.attrs)
# ou
print(soup.h1.attrs)

print("li - lista")
li = soup.li
print(li)
print("---Atributos----")
print(li.attrs)
print(li.a['href'])
# ou
print(li.a.get('href'))

print(li.get_text())
# ou
print(li.a.string)
