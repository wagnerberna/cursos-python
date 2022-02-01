from bs4 import BeautifulSoup
import requests

import requests

url = 'https://i.ytimg.com/vi/-oYMo8k22Vw/maxresdefault.jpg'

req = requests.get(url)

with open('img.jpg', 'wb') as f:
	f.write(req.content)