# *args **kwargs
def todos_params(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


# todos param. posicionais p/ Tupla *args
todos_params("a", "b", "c")
# Todos param. nomeados p/ Dict **args
todos_params(a=1, b=2, c=3)
todos_params(1, 2, 3, legal=True, valor=12.99)
todos_params("Wagner", "Aline", False, [1, 2, 3], Fragil=True, valor=12.99)
