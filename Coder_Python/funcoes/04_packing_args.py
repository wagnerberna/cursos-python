# Unpacking
def soma_3(a, b, c):
    return a + b + c


tupla_num = (5, 2, 3)
print(soma_3(*tupla_num))

lista_num = [5, 2, 3]
print(soma_3(*lista_num))

# Packi]g * (tupla de ºn)
def soma_n(*numeros):
    soma = 0
    print(numeros)
    for n in numeros:
        soma += n
    return soma


print(soma_n(1))
print(soma_n(2, 3, 5))
