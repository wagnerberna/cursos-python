def fibonacci(quantidade, sequencia=(0, 1)):
    # print(sequencia)
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


for fib in fibonacci((8)):
    print(fib)
