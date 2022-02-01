# split (dividir uma string)
# join (Juntar uma lista)
# Enumerate (enumerar el da lista )
frase = "Penso, logo existo"
lista = frase.split(" ")
lista2 = frase.split(",")
print(lista, lista2)

lista3 = "/".join(frase)
print(lista3)

lista_nomes = ["wagner", "aline", "cris"]
for indice, valor in enumerate(lista_nomes):
    print(indice, valor)
