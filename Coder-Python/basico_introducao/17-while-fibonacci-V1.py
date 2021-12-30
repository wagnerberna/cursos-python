# seq de fibonacci próx. núm soma do anterior
# 0, 1, 2, 3, 5, 8, 12, 21 ....
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f"{penultimo}, {ultimo}", end=",")
    while ultimo < limite:
        proximo = penultimo + ultimo
        print(proximo, end=",")
        penultimo = ultimo
        ultimo = proximo


fibonacci(1000)
