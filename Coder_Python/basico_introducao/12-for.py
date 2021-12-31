# Cria classe c/ cor vermelha e normal
class TerminalColor:
    ERRO = "\033[91m"
    NORMAL = "\033[0m"


# range o último número não entra
def faixa_etaria(idade):
    try:
        idade = float(idade)
        if 0 <= idade < 18:
            return "Menor de idade"
        elif idade in range(18, 65):
            return "Adulto"
        elif idade in range(65, 100):
            return "Idoso"
        elif idade >= 100:
            return "Centenário"
        else:
            return "Idade inválida"
    except ValueError:
        print(
            TerminalColor.ERRO
            + """Erro:
        idade deve ser numérico!"""
            + TerminalColor.NORMAL
        )


# for idade in (0, 17, 20, 65, 100, 101, -2, "bla"):
#     print(f"{idade}: {faixa_etaria((idade))}")
# ou
tupla_idades = (0, 17, 20, 65, 100, 101, -2, "bla")
for idade in tupla_idades:
    print(f"{idade}: {faixa_etaria((idade))}")
