# Parâmetros Opcionais
# FN para criar um bloco HTML
# parâmetros texto, e classe
# Param. Opc. classe, se nada for passado pega o padrão
def tag_bloco(texto, classe="success"):
    return f'<div class="{classe}">{texto}</div>'


print(tag_bloco("Batman vs Superman"))
