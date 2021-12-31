from a01_fn_first_class import dobro, quadrado

# fn imprime titulo, e executa a fn p/ cada el da lista
def processar(titulo, lista, funcao):
    print(f"Processando: {titulo}")
    print(f"Nome Função: {funcao.__name__} ")
    for i in lista:
        print(f"{i} => {funcao(i)}")


processar("dobro de 1 a 10", range(1, 11), dobro)
processar("dobro de 1 a 10", range(1, 11), quadrado)
