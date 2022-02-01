from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

print(soup.li.parent)

# irmãos do mesmo nível da árvore, não da mesma tag
print("---Acessando próximo irmãos---")
print(soup.li.next_sibling.next_sibling)

print(soup.li.parent)
print("---Acessando irmão anterior---")
print(soup.li.previous_sibling.previous_sibling)

print("---FOR Acessando irmãos---")
for sibling in soup.li.next_siblings:
    print(repr(sibling))
