# generator_v1 - ()
# (expressão + for item in list + condição)
generator = (i * 2 for i in range(10) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) #Gera Erro

# for sem usar next
for numero in generator:
    print(numero)
