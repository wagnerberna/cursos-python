PALAVRAS_PROIBIDAS = {"futebol", "religião", "política"}
textos = [
    "Wagner gosta de debater política e RELIGIÃO",
    "Wagner gosta de praia",
]
# busca palavras proibidas
# Break interrompe o 2º for caindo no else
for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print("Palavra proibida detectada:", intersecao)
    else:
        print("Texto liberado:", texto)