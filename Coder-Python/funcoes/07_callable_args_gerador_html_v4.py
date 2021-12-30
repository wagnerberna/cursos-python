# FN p/ criar uma tag UL com os elementos LI
# Generator p/ criar elementos da lista
# Retorna uma UL com a lista gerada
def tag_lista(*itens):
    lista = "".join(f"<li>{item}</li>" for item in itens)
    return f"<ul>{lista}</ul>"


# FN para gerar TAG com o conteúdo da UL
# Novo parâmetro *args
# html recebe conteudo caso não seja callable, se for chama conteudo passando os args
def tag_bloco(conteudo, *args, classe="success", inline=False):
    tag = "span" if inline else "div"
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


# print(tag_bloco("Batman vs Superman", "info", True))
# chama FN do bloco e passa a outra FN como parâmetro
print(tag_bloco(tag_lista("item 1", "item 2"), classe="info"))
# passa a FN tag_lista e seus param. na seq. *args, identifica classe
print(tag_bloco(tag_lista, "item 1", "item 2", classe="info", inline=True))
