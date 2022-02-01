# Cria classe c/ cor vermelha e normal
class TerminalColor:
    ERRO = "\033[91m"
    NORMAL = "\033[0m"


def valida_nota(nota):
    try:
        nota = float(nota)
        if nota >= 9:
            print("CDF")
        elif nota >= 7:
            print("Aprovado")
        elif nota >= 5:
            print("Recuperação")
        else:
            print("Reprovado")
    except ValueError:
        print(
            TerminalColor.ERRO
            + """Erro:
        Nota deve ser numérico!"""
            + TerminalColor.NORMAL
        )


valida_nota(input("Digite a Nota:"))
