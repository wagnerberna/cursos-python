from bs4 import BeautifulSoup
from bs4 import NavigableString, Tag
import requests

endpoint = 'http://www.mercadolivre.com/'
req = requests.get(endpoint)
# cria instância do BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

# código 301 redirecionamento
print (req.history)

print (req.history[1].headers)
print('--------')
# local de redirecionamento ".com.br"
print (req.history[1].headers['location'])

