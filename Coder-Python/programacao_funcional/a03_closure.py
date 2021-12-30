# fn q retorna outra
def multiplicar(x):
    def calcular(y):
        return x * y

    return calcular


# param passados em 1 vez
print(multiplicar(2)(7))
# fn armazenada em uma var
# param. passados de forma parcial1
dobro = multiplicar(2)
triplo = multiplicar(3)
print(dobro)
print(triplo)
# param. final para executar
print(f"o dobro de 7 é {dobro(3)} ")
print(f"o triplo de 3 é {triplo(3)} ")
