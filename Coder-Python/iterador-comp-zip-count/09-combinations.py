from itertools import combinations, permutations, product

herois = ["Bruce", "Clark", "Diana", "Jonh", "Lex"]

# combinations
# Todas combinações possíveis
# Sem repetir os pares, ou 1 nome em 2 posições
for grupo in combinations(herois, 2):
    print(grupo)

# permutation
# Todas combinações possíveis
# Repetindo os pares em ordem diferente
# Sem repetir 1 nome em 2 posições
for grupo in permutations(herois, 2):
    print(grupo)

# product
# Todas combinações possíveis
# Repetindo os pares em ordem diferente
# Repetindo 1 nome em 2 posições
for grupo in product(herois, repeat=2):
    print(grupo)
