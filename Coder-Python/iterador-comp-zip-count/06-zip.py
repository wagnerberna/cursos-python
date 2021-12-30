from itertools import count

# zip - une até o limite de itens da menor lista
# gerador de indices
indice = count()
estados = ["RS", "SC", "BA"]
cidades = ["Caxias do sul", "Florianópolis", "Bahia", "Porto Alegre"]

cidades_estados = zip(indice, cidades, estados)
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

# for valor in cidades_estados:
#     print(valor)

lista_cidades_estados = list(cidades_estados)
print(lista_cidades_estados)
# dict_cidades_estados = dict(cidades_estados)
# print(dict_cidades_estados)

# Somando 1 item de cada lista em uma nova no limite da menor
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
uniao_ab = list(zip(lista_a, lista_b))
print(uniao_ab)
soma = [x + y for x, y in uniao_ab]
print(soma)
