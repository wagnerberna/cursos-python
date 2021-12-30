# callable FN passada como callback, chamada dentro da fn
def executar(fn1, fn2):
    if not callable(fn1) and not callable(fn2):
        return print("parâmetros não são funções")
    fn1()
    fn2()


def bom_dia():
    print("bom dia!")


def boa_tarde():
    print("boa tarde!")


executar(bom_dia, boa_tarde)
executar(1, 5)
