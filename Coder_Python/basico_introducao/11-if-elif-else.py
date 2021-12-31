# Cria classe c/ cor vermelha e normal
class TerminalColor:
    ERRO = "\033[91m"
    NORMAL = "\033[0m"


def faixa_etaria(idade):
    try:
        idade = float(idade)
        if 0 <= idade < 18:
            return "Menor de idade"
        elif idade in range(18, 64):
            return "Adulto"
        elif idade in range(65, 99):
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


print(faixa_etaria(input("Digite a Idade:")))
