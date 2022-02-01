# Parâmetros Opcionais
# FN para criar um bloco HTML
# parâmetros texto, e classe
# Param. Opc. classe, se nada for passado pega o padrão
def tag_bloco(texto, classe="success"):
    return f'<div class="{classe}">{texto}</div>'


# Testes (assertions)

assert (
    tag_bloco("Incluído com sucesso!")
    == '<div class="success">Incluído com sucesso@@@!</div>'
)
