# importar a função randint (gera randômico inteiro) do random
from random import randint

num_randomico = randint(0, 9)
num_user = -1

# enquanto expressão for vdd executa o loop
while num_user != num_randomico:
    num_user = int(input("Tente adivinhar um número de 0 a 9:"))

print(f"Vc acertou o número é {num_randomico}")
