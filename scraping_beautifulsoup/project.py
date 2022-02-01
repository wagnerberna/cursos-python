from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

# endpoint geral:

page = 1
endpoint_primary = f'https://sample-university-site.herokuapp.com/approvals/{page}'
req_primary = requests.get(endpoint_primary)

soup_primary = BeautifulSoup(req_primary.text, 'lxml')

print("---FOR para pegar os Filhos----")
for child in soup_primary.body.contents:
    if child.name == 'li':
        print(child)
        print(child.a.get('href'))
        print(child.get_text())


# endpoint candidatos

candidate_cpf = '178.422.117-11'
endpoint_candidate = f'https://sample-university-site.herokuapp.com/candidate/{candidate_cpf}'
req_candidate = requests.get(endpoint_candidate)

print(req_candidate.url)

# cria instância do BeautifulSoup
soup_candidate = BeautifulSoup(req_candidate.text, 'lxml')

# print(soup_candidate)
path_name = soup_candidate.div.next_element
# print(path_name)
name = path_name.next_element.next_element
print(name)
path_score = soup_candidate.div.next_sibling.next_sibling.next_element
# print(path_score)
score = path_score.next_element.next_element
print(score)
