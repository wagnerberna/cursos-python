import re

texto = """
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> 
"""

# Metacaracteres greedy / Non-greedy (Gulosos/preguiçoso): .* .+ .*?
# Meta caracteres:
# .* 0 ou n
# .+ 1 ou n
# xx? 0 ou 1 (preguiçoso, busca o mín. de info para fechar a expressão)
# localiza as tags < > q podem ter de 1 a 3 leltras
print(re.findall(r"<[pdiv]{1,3}>", texto))
# abre tag p/ pegar conteúdo das tags c/ tags:
# .* (dot all . qualquer coisa * n vezes )
# "guloso" busca o máx. de info possíveis
print(re.findall(r"<[pdiv]{1,3}>.*", texto))
# \/ fecha tag "/" usar barra na frente.
print(re.findall(r"<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>", texto))
# ? (preguiçoso, busca o mín. de info para fechar a expressão)
# gera array el por tag
print(re.findall(r"<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>", texto))
# .+ não pega a div vazia
print(re.findall(r"<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>", texto))
