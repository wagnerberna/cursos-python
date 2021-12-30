import re

texto = "Mais um belo dia de sol no paraíso mais belo do mundo"
# Em cada execução o phyton compila a regex
# search busca primeira ocorrência
print(re.search(r"belo", texto))
# findall busca todas ocorrências
print(re.findall(r"belo", texto))
# sub substituir todos itens / count núm. de ocorrências p/ substituir
print(re.sub(r"belo", "ABC", texto))
print(re.sub(r"belo", "ABC", texto, count=1))

# compile compila 1 só vez a regex e armazena em uma var
regex = re.compile(r"belo")
print(regex.search(texto))
print(regex.findall(texto))
print(regex.sub("ABC", texto))
