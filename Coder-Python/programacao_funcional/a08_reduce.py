from functools import reduce

pessoas = [
    {"nome": "Wagner", "idade": 40},
    {"nome": "Aline", "idade": 15},
    {"nome": "Cris", "idade": 17},
    {"nome": "Tânia", "idade": 60},
    {"nome": "Carlinhos", "idade": 70},
]

soma_idades = reduce(lambda ac, el: ac + el["idade"], pessoas, 0)
print(soma_idades)
