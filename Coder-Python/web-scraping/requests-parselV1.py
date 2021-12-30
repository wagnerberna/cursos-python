import requests
from parsel import Selector


# getAll captura todos
# get captura o 1º
def fetch_test_for(url):
    try:
        response = requests.get(url, timeout=2)
        print(f"Status: {response.status_code}")
        sel = Selector(text=response.text)
        print(sel)
        # array com todas imagens / item 0:
        get_all = sel.css("img.thumbnail").getall()
        print(get_all)
        get_el = sel.css("img.thumbnail").getall()[0]
        # print(get_el)
        get_one = sel.css("img.thumbnail").get()
        print(get_one)
        for index, el in enumerate(get_all):
            print(f"Elemento nº {index}")
            print(el)
        # print(list(map(lambda el: el, get_all)))
    except requests.ReadTimeout:
        print(f"Erro: {response.status_code}")


# site p/ testes: http://books.toscrape.com/
fetch_test_for("http://books.toscrape.com/")
