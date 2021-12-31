try:
    arquivo = open("./manipulacao_arquivos/pessoas.csv")

    for dado in arquivo:
        print("Nome: {}, Idade: {}".format(*dado.strip().split(",")))
except IndexError:
    pass
finally:
    print("finally fecha o arquivo")
    arquivo.close()

if arquivo.closed:
    print("Arquivo já foi fechado!")
