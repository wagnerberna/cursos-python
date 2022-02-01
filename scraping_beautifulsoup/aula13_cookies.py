from bs4 import BeautifulSoup
import requests

# ERRO

url = 'http://www.submarino.com.br/'


r = requests.get(url)
cookie = r.cookies.get_dict()

print(cookie)

# busca = 'notebook'
# url = 'http://busca.submarino.com.br/busca.php?q={0}'.format(busca)

# r = requests.get(url, cookies=cookie)
# with open('submarino.html', 'w') as f:
# 	f.write(r.text)