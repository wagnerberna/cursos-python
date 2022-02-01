from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

print("---find_parent / find_parents---")
# find_parent (find para pais)
# find_parents (find_all para pais)
find_tag_pai = soup.li.find_parent()
print(find_tag_pai)

print("---find_parent / find_parents---")
find_tag_pais = soup.li.find_parents()
print(find_tag_pais)
