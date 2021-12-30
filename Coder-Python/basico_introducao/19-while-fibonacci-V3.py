# seq de fibonacci próx. núm soma do anterior
# 0, 1, 2, 3, 5, 8, 12, 21 ....
def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado


print(fibonacci(1000))
