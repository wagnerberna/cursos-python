def fibonacci(quantidade, sequencia=(0, 1)):
        return sequencia if len(sequencia) == quantidade else
            fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

# Trava!!!
for fib in fibonacci((8)):
    print(fib)
