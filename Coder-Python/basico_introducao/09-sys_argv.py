import sys
import errno


def calcula_ano_nasc(idade):
    print(sys.argv)
    # print(sys.argv[1])
    print(idade)
    # exit finaliza o script
    sys.exit(errno.EPERM)
    sys.exit(1)
    ano = 2021 - idade
    return ano
