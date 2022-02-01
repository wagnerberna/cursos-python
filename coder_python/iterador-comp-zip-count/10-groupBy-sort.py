from itertools import groupby, tee

alunos = [
    {"nome": "Luiz", "nota": "A"},
    {"nome": "Letícia", "nota": "B"},
    {"nome": "Fabrício", "nota": "A"},
    {"nome": "Rosemary", "nota": "C"},
    {"nome": "Joana", "nota": "D"},
    {"nome": "João", "nota": "A"},
    {"nome": "Eduardo", "nota": "B"},
    {"nome": "André", "nota": "C"},
    {"nome": "Anderson", "nota": "B"},
]
# groupBy precisa que a lista esteja ordenada
# ordenar por nota
# alunos.sort(key=lambda item: item["nota"])
# print(list(alunos))

# Agrupar por nota
# alunos_agrupados = groupby(alunos, lambda item: item["nota"])
# print(list(alunos_agrupados))

# Código Refatorado
ordenar = lambda item: item["nota"]
alunos.sort(key=ordenar)
# print(list(alunos))
alunos_agrupados = groupby(alunos, ordenar)
# print(list(alunos_agrupados))

# for agrupamento_notas, valores_agrupados in alunos_agrupados:
#     qtde = len(list(valores_agrupados))
#     print(f"{qtde} alunos tiraram nota: {agrupamento_notas}")


# for agrupamento_notas, valores_agrupados in alunos_agrupados:
#     print(f"Nota:{agrupamento_notas}")
#     for aluno in valores_agrupados:
#         print(f"Aluno: {aluno}")

# tee (faz cópias "cp" do iterador)
for agrupamento, valores_agrupados in alunos_agrupados:
    v1, v2 = tee(valores_agrupados)

    print(f"Agrupamento: {agrupamento}")

    for aluno in v1:
        print(f"\t{aluno}")

    quantidade = len(list(v2))
    print(f"\t{quantidade} alunos tiraram nota {agrupamento}")

# map_alunos = list(map(lambda el: f"Nota:{el} ", alunos_agrupados))
# print(map_alunos)
