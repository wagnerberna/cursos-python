# continue (interrompe a repetição atual do laço)
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)

# break(interrompe todo laço)
for num in range(1, 11):
    if num == 6:
        break
    print(num)

# usando Tupla e Lista
PALAVRAS_PROIBIDAS = ("futebol", "religião", "política")
textos = [
    "Wagner gosta de debater política e RELIGIÃO",
    "Wagner gosta de praia",
]
# busca palavras proibidas
# Break interrompe o 2º for caindo no else
for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Palavra proibida detectada:", palavra)
            break
    else:
        print("Texto liberado:", texto)
