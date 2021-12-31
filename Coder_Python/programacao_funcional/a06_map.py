lista_1 = [1, 2, 3]
dobro = map(lambda el: el * 2, lista_1)
print(list(dobro))

lista_2 = [
    {"nome": "Wagner", "idade": 40},
    {"nome": "Aline", "idade": 18},
    {"nome": "Cris", "idade": 30},
]

so_nomes = map(lambda el: el["nome"], lista_2)
print(list(so_nomes))

so_idades = map(lambda el: el["idade"], lista_2)
print(sum(so_idades))

# desafio
desafio = map(lambda el: f'{el["nome"]} tem {el["idade"]} anos', lista_2)
print(list(desafio))
