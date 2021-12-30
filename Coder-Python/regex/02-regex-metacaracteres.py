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
"""
# Metacaracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
print(re.findall(r"joão|Maria|adultos", texto))
# Flags IGNORECASE (ignora maiúsculo e minúsculo)
# re.I ou re.IGNORECASE
print(re.findall(r"joão|Maria|adultos", texto, flags=re.IGNORECASE))
# . (Qualquer caractere (com exceção da quebra de linha))
print(re.findall(r".oão|.aria|ad.lto.", texto))
# [] (conjunto de caracteres q podem ocupar aquela posição)
# (permite usar range de caracteres ou números diferencia maiúsculo)
print(re.findall(r"[Jj]oão|[Mm]aria", texto))
print(re.findall(r"[a-zA-Z]oão|[a-zA-Z0-9]aria", texto))
