import csv

# importar request para poder baixar o arquivo
from urllib import request


def read_file(url):
    with request.urlopen(url) as entrada:
        print("Baixando o CSV...")
        # ler arquivo na codificação ISO-8859(latin1)
        dados = entrada.read().decode("latin1")
        print("Download completo!")
        for cidade in csv.reader(dados.splitlines()):
            print(f"{cidade[8]} : {cidade[3]}")


# "r" impede que caracteres especiais sejam interpretados pelo código, faz a leitura literal
read_file(r"http://files.cod3r.com.br/curso-python/desafio-ibge.csv")
