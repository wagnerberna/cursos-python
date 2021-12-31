pessoas = [
    {"nome": "Wagner", "idade": 40},
    {"nome": "Aline", "idade": 15},
    {"nome": "Cris", "idade": 17},
    {"nome": "Tânia", "idade": 60},
    {"nome": "Carlinhos", "idade": 70},
]

# menores de 18 anos
menores = filter(lambda el: el["idade"] < 18, pessoas)
print(list(menores))

# Nomes com mais de 6 caracteres
nomes_grandes = filter(lambda el: len(el["nome"]) > 5, pessoas)
print(list(nomes_grandes))
