from bs4 import BeautifulSoup
import requests

# ERRO

url = 'http://compras.dados.gov.br'
cnpj = '07689002000189' #Embraer

url = '{0}/contratos/v1/contratos.json?cnpj_contratada={1}'.format(url, cnpj)

r = requests.get(url)
print(r.json())
# print(r.json()['_embedded']['contratos'])
# print(r.json()['_embedded']['contratos'][0])