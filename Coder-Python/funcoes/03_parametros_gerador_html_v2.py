# Parâmetros Nomeados
def tag_bloco(texto, classe="success", inline=False):
    tag = "span" if inline else "div"
    return f'<{tag} class="{classe}">{texto}</{tag}>'


print(tag_bloco("Batman vs Superman", "info", True))
# pode alterar a ordem de passagem desde q faça atribuição
print(tag_bloco("Batman vs Superman", inline=True, classe="info"))
