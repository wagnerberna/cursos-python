# Tupla dentro de dicionário definir se dia é:
# final de semana (valor 1 e 7)
# Dia da semana (range de 1 a 7) ultimo valor não entra
def get_tipo_dia(dia):
    dias = {
        (1, 7): "Fim de semana",
        tuple(range(2, 7)): "dia de semana",
    }
    # Generator:
    # numeros valor são os numeros da tupla
    # tipo chave são as strings "fim d...."
    # chave: valor / tupla: string / numeros: tipo
    # se dia estiver dentro dos numeros
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, "Dia inválido")


for dia in range(0, 9):
    print(f"{dia}: {get_tipo_dia(dia)} ")
