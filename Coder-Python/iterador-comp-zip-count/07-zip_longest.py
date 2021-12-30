# zip_longest - unir listas
from itertools import zip_longest, count

# zip - une até o limite de itens da maior lista
estados = ["RS", "SC", "BA"]
cidades = ["Caxias do sul", "Florianópolis", "Bahia", "Porto Alegre"]

cidades_estados = zip_longest(cidades, estados, fillvalue="Outros")

lista_cidades_estados = list(cidades_estados)
print(lista_cidades_estados)
# dict_cidades_estados = dict(cidades_estados)
# print(dict_cidades_estados)

# Somando 1 item de cada lista C/ valor padrão 0
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
uniao_ab = list(zip_longest(lista_a, lista_b, fillvalue=0))
print(uniao_ab)
soma = [x + y for x, y in uniao_ab]
print(soma)
