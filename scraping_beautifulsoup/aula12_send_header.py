import requests
from bs4 import BeautifulSoup

url = 'http://michaelis.uol.com.br/busca?'

payload = {'r':'0',
			'f':'0',
			't':'0',
			'palavra':'talk'}

header = {'(Request-Line)':'GET /busca?r=0&f=0&t=0&palavra=talk HTTP/1.1',
		'Host':	'michaelis.uol.com.br',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding':'gzip, deflate',
		'Referer':'http://michaelis.uol.com.br/'}

r = requests.get(url, params=payload, headers=header)

soup = BeautifulSoup(r.text, 'lxml')

div = soup.find('div', {'id':'content'})
print(div.get_text())

with open('michaelis.html', 'w', encoding='utf-8') as f:
	f.write(r.text)

print(r.request.headers)