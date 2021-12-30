# FN p/ criar uma tag UL com os elementos LI
# Generator p/ criar elementos da lista
# Retorna uma UL com a lista gerada
def tag_lista(*itens):
    lista = "".join(f"<li>{item}</li>" for item in itens)
    return f"<ul>{lista}</ul>"


# FN para gerar TAG com o conteúdo da UL
def tag_bloco(conteudo, classe="success", inline=False):
    tag = "span" if inline else "div"
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


# print(tag_bloco("Batman vs Superman", "info", True))
# chama FN do bloco e passa a outra FN como parâmetro
print(tag_bloco(tag_lista("item 1", "item 2"), "info"))
