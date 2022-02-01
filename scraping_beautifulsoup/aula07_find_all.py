from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

# localiza a primeira tag
print("---find_all---")
find_tag_list = soup.find_all('li')
print(find_tag_list)


print("---find_all limitando a busca---")
find_tag_limit = soup.find_all('li', limit=2)
print(find_tag_limit)

print("---find_all busca por string---")
find_tag_string = soup.find_all(string=['12', '45', '59'])
print(find_tag_string)

print("---find_all busca por string---")
find_tag_string2 = soup.find_all('li', string=True)
print(find_tag_string2)


print("---find_all busca por TAG---")
find_tag_list_li_a = soup.li.a.find_all(string=True)
print(find_tag_list_li_a)
