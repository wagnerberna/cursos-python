arquivo = open("./manipulacao_arquivos/pessoas.csv")

for dado in arquivo:
    print("Nome: {}, Idade: {}".format(*dado.strip().split(",")))

arquivo.close()
