from itertools import count

contador = count(start=5, step=-2)

for valor in contador:
    print(round(valor, 2))
    # if 0 <= valor >= 10:
    if valor <= -10 or valor >= 10:
        break

indice = count(start=1)
lista_nomes = ["Wagner", "Aline", "Cris"]
relatorio = list(zip(indice, lista_nomes))
print(relatorio)
