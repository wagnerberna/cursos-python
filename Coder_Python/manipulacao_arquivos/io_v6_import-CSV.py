import csv

with open("./manipulacao_arquivos/pessoas.csv", "r") as arquivo_entrada:
    with open("./manipulacao_arquivos/pessoas.txt", "w") as arquivo_saida:
        for pessoa in csv.reader(arquivo_entrada):
            print("Nome: {}, Idade: {}".format(*pessoa), file=arquivo_saida)

if arquivo_entrada.closed:
    print("Arquivo já foi fechado!")
if arquivo_saida.closed:
    print("Arquivo já foi fechado!")
