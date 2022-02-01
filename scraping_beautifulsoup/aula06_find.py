from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

# localiza a primeira tag
print("---find---")
find_tag = soup.find('li')
print(find_tag)


find_text = soup.find(string='178.422.117-11')
print(find_text)


# busca por id, class, etc...
find_href = soup.find(href="/candidate/178.422.117-11")
print(find_href)
