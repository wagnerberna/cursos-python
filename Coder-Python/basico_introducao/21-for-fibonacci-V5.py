# seq de fibonacci próx. núm soma do anterior
# 0, 1, 2, 3, 5, 8, 12, 21 ....
# range começa com 2 el e vai até a quantidade
# "_" uma variável não usada
def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
    return resultado


print(fibonacci(8))
