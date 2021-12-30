with open("./manipulacao_arquivos/pessoas.csv") as arquivo:

    for dado in arquivo:
        print("Nome: {}, Idade: {}".format(*dado.strip().split(",")))

if arquivo.closed:
    print("Arquivo já foi fechado!")
