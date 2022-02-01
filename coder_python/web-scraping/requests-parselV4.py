import requests
from parsel import Selector


def fetch_test_for(url):
    try:
        response = requests.get(url, timeout=2)
        print(f"Status: {response.status_code}")
        sel = Selector(text=response.text)

        getall_url_books = sel.css(
            "div.image_container a::attr(href)"
        ).getall()
        print(getall_url_books)

        for url_book in getall_url_books:
            response_url_book = requests.get(
                f"http://books.toscrape.com/{url_book}"
            )
            sel_url_book = Selector(text=response_url_book.text)
            book_title = sel_url_book.css("div.product_main h1").get()
            print(book_title)

    except requests.ReadTimeout:
        print(f"Erro: {response.status_code}")


# site p/ testes: http://books.toscrape.com/
fetch_test_for("http://books.toscrape.com/")
