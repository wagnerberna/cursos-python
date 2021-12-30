from functools import reduce

pessoas = [
    {"nome": "Wagner", "idade": 40},
    {"nome": "Aline", "idade": 15},
    {"nome": "Cris", "idade": 17},
    {"nome": "Tânia", "idade": 60},
    {"nome": "Carlinhos", "idade": 70},
]

# filter / reduce
# somar idade das menores de idade
menores = list(filter(lambda el: el["idade"] < 18, pessoas))
soma_idades_menores = reduce(lambda ac, el: ac + el["idade"], menores, 0)

# print(menores)
# print(soma_idades_menores)

# map / filter / reduce
# primeiro filtrar as idades
# idades = map(lambda el: el["idade"], pessoas)
so_idades = list(map(lambda el: el["idade"], pessoas))
menores2 = list(filter(lambda el: el < 18, so_idades))
soma_idades = reduce(lambda ac, el: ac + el, menores2, 0)

print(so_idades)
print(menores2)
print(soma_idades)
