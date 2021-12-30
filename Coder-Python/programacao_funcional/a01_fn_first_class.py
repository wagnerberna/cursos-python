def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


# atribuir em uma var
d = dobro
# print(d(5))

# Armazenar fn dentro de uma lista
# Repetir 5X cada uma das FN
func = [dobro, quadrado] * 5

# zip junta fn com dado
# range de 1 a 10 fornece param "numero" para calculo
# retorna altenadamente o dobro ou quadrado de 1 a 10
# for func, numero in zip(func, range(1, 10)):
#     print(f"{func.__name__} de {numero} é {func(numero)}")
