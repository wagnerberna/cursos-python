# FN LOG retorna um Decorator ()
def log(function):
    def decorator(*args, **kwargs):
        print(f"inicio da chamamada da FN: {function.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        resultado = function(args, kwargs)
        print(f"Resultado da chamada:{resultado}")
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


print(soma(3, 2))
print(sub(3, y=2))