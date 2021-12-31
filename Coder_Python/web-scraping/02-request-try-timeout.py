import requests
import time


def fetch_test_limit_request(url, timeout=5):
    for _ in range(15):
        response = requests.get(url)
        print(response)
        time.sleep(5)


# fetch_test_limit_request("https://www.cloudflare.com/rate-limit-test/")


def fetch_test_timeout(url):
    # time.sleep(2)
    try:
        response = requests.get(url, timeout=2)
        print(f"Tentativa1: {response.status_code}")
    except requests.ReadTimeout:
        response = requests.get(url, timeout=4)
        print(f"Tentativa2: {response.status_code}")
    finally:
        print(response.status_code)


# site/x define o tempo de resposta
fetch_test_timeout("http://httpbin.org/delay/3")
