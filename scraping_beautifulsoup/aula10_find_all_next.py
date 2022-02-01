from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'https://sample-university-site.herokuapp.com/approvals/1'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

# AJUSTAR EXEMPLOS

producers = soup.find(id='producers')
tag_next = producers.find_next()
print(tag_next)

producers = soup.find(id='producers')
tag_next = producers.find_all_next()
print(tag_next)

producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_previous()
print(tag_previous)


producers = soup.find(id='quaternaryconsumers')
tag_previous = producers.find_all_previous()
print(tag_previous)
