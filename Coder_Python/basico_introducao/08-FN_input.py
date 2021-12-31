# Renomear para importar
def calcula_ano_nasc(idade):
    return 2021 - idade


nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
print(nome, idade)
print(f"Data de nascimento {2021 - idade}")
print(f"Data de nascimento {calcula_ano_nasc(idade)}")
