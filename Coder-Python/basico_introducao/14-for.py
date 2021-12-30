# imprimir el de 1 a 5
for i in range(1, 6):
    print(f"i = {i}")
# ou
for i in range(6):
    print(f"i = {i}")

# Imprimir Tabuada
for x in range(1, 11):
    for y in range(1, 11):
        print(f"{x} * {y} = {x*y} ")

# for string
palavra = "constituição"
for letra in palavra:
    print(letra)

# for string na mesma linha
palavra = "constituição"
for letra in palavra:
    print(letra, end=",")

# lista
membros = ["Wagner", "Aline", "Thor", "Tuca", "Pitty", "Ravena", "Pink"]
for nome in membros:
    print(nome, end=" ")

# Lista Enumerate
membros = ["Wagner", "Aline", "Thor", "Tuca", "Pitty", "Ravena", "Pink"]
for index, nome in enumerate(membros):
    print(index + 1, nome, end=" ")

# Tupla
dias_semana = (
    "Domingo",
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado",
)
for dia in dias_semana:
    print(f"dia: {dia}", end=" / ")

# dicionário
pessoa1 = {"nome": "Aline", "idade": 20}
pessoa2 = {"nome": "Wagner", "idade": 40, "cursos": ["udemy", "trybe"]}

# dic. Chave
for chave in pessoa2:
    print(chave)
# ou
for chave in pessoa2.keys():
    print(chave)

# dic. Valor
for valor in pessoa2.values():
    print(valor)

pessoa2 = {"nome": "Wagner", "idade": 40, "cursos": ["udemy", "trybe"]}
# dic. Chave e Valor
for chave, valor in pessoa2.items():
    print(chave, "=", valor)

print(f"ultima chave e valor disponíveis fora do for: {chave} e {valor} ")
