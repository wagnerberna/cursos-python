# seq de fibonacci próx. núm soma do anterior
# 0, 1, 2, 3, 5, 8, 12, 21 ....
# definir a quantidade de números gerados e não o limite
# usa while True (infinito) + break
def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


print(fibonacci(8))
