import requests
from parsel import Selector


# getAll captura todos
# get captura o 1º
def fetch_test_for(url):
    try:
        response = requests.get(url, timeout=2)
        print(f"Status: {response.status_code}")
        sel = Selector(text=response.text)
        get_div = sel.css("div.image_container").get()
        print(get_div)
        get_div_atributo = sel.css("div.image_container a::attr(href)").get()
        print(get_div_atributo)
        get_div_atributo = sel.css("div.image_container img::attr(src)").get()
        print(get_div_atributo)
    except requests.ReadTimeout:
        print(f"Erro: {response.status_code}")


# site p/ testes: http://books.toscrape.com/
fetch_test_for("http://books.toscrape.com/")
