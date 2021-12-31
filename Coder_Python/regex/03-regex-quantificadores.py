import re

texto = """
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
Jãooooooo
"""
# Metacaracteres Quantificadores: * + ? { }
# * (0 ou n vezes)
# + (1 ou n vezes)
# -1º"o" pode repetir 0 ou n vezes ou não existir 0x
# -2º"o" pode repetir 2 ou n vezes
print(re.findall(r"jo*ão{2,}", texto, flags=re.I))
# -pode aplicar a conjuntos de caracteres ex: [a-z]+
print(re.findall(r"jo+ã[a-z]+", texto, flags=re.I))
# {1,} (1 ou n vezes)
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {n} x vezes num. específico
# {min, max} min e máx de vezes
# {5,10} De 5 a 10
# -"e"  deve repetir 3x e "m" de 1 até 2x
print(re.findall(r"ve{3}m{1,2}", texto, flags=re.I))

texto2 = "João ama ser amado"
# localiza com letras "o" ou "d" q podem repetir de 0 a 2x
print(re.findall(r"ama[od]{0,2}", texto2, flags=re.I))

# ? 0 ou 1
# ()+ [a-zA-Z0-9]+