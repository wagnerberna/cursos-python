from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

print("---find_next_sibling / find_next_sibling busca irmãos---")
find_tag_irmao = soup.li.find_next_sibling()
print(find_tag_irmao)
print("---find_next_siblings / find_next_siblings busca TODOS irmãos---")
find_tag_irmaos = soup.find_next_siblings()
print(find_tag_irmaos)
