# Listas [] / Array
lista = []
print(type(lista))
print(len(lista))
# Add / Remove
lista.append(1)
lista.append(2)
print(lista)
lista.remove(2)
lista.append(3)
lista.append("wb")
# Inverter Lista altera a própria lista original
lista.reverse()

# index / in (membro)
lista2 = [1, 5, "Wagner", "Aline", 3.14]
index_protagonista = lista2.index("Wagner")
protagonista = lista2[2]
protagonista = lista2[-3]

protagonista_existe = "Wagner" in lista2
num_3_nao_existe = 3 not in lista2

lista_nomes = lista2[2:4]
lista_pulando_1el = lista2[::2]

# Del por index
lista3 = [1, 5, "Wagner", "Aline", 3.14]
del lista3[2:4]
