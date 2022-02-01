# FN p/ criar uma tag UL com os elementos LI

# tuplas para filtrar os atributos do bloco e os da UL:
bloco_atributos = ("bloco_accesskey", "bloco_id")
ul_atributos = ("lista", "ul_style")

# FN Gerador retirar bloco_ e ul_ dos atributos informados
# retorna chave = valor
# if para só aplicar se a chave estiver dentro da tupla
def filtrar_atributos(info, suportados):
    # print(info)
    return " ".join(
        f'{key.split("_")[-1]}="{value}"'
        for key, value in info.items()
        if key in suportados
    )


# Generator p/ criar elementos da lista
# Retorna uma UL com a lista gerada
def tag_lista(*itens, **kwargs):
    lista = "".join(f"<li>{item}</li>" for item in itens)
    return f"<ul {filtrar_atributos(kwargs, ul_atributos)}>{lista}</ul>"


# FN para gerar TAG com o conteúdo da UL
# Novo parâmetro *args
# html recebe conteudo caso não seja callable, se for chama conteudo passando os args
# conteudo a FN tag_lista q só vai ser executada se for uma callable
def tag_bloco(conteudo, *args, classe="success", inline=False, **kwargs):
    print(f"var conteudo:  {conteudo}")
    tag = "span" if inline else "div"
    html = conteudo if not callable(conteudo) else conteudo(*args, **kwargs)
    print(f"var html:  {html}")
    atributos = filtrar_atributos(kwargs, bloco_atributos)
    print("Retorno FN:")
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


# atributo blabla não consta na lista não é aplicado
print(
    tag_bloco(
        tag_lista,
        "item 1",
        "item 2",
        classe="info",
        bloco_accesskey="m",
        bloco_id="conteudo",
        ul_id="lista",
        ul_style="color:red",
        blabla="bla",
    )
)
