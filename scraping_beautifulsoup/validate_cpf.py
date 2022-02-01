# https://programandoautomacao.blogspot.com/2020/10/python-uma-funcao-pythonica-para.html
# https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/


def validate_cpf(cpf_candidate):
    cpf_length = 11
    cpf = ''.join([(char) for char in cpf_candidate if char.isdigit()])
    print(type(cpf))
    print(cpf)

    if len(cpf) != cpf_length:
        return False

    # A Comp irá interear sobre cada valor da string "1234567890"
    # multiplica cada caracter da string "1234567890" pelo tamanho gerando um cpf todo repetido
    # se string criando uma lista com todos cpfs repetidos possíveis
    # se o CPF estiver nessa lista é falso
    print('comprehension:::')
    print(list((char * cpf_length for char in "1234567890")))
    if cpf in (char * cpf_length for char in "1234567890"):
        return False

    # inverte o CPF
    cpf_reverse = cpf[::-1]
    print(cpf_reverse)

    print('FOR::::')
    # for i vai de 2 e 1
    for i in range(2, 0, -1):
        print(f'count i:::{i}')
        print('enumerado:::')
        # cria uma tupla enumerada com cpf invertido iniciando no 3 pula os dig. verificadores
        # [(2, '0'), (3, '5'), (4, '3'), (5, '6'), (6, '1'), (7, '2'), (8, '6'), (9, '0'), (10, '8')]
        cpf_enumerate = enumerate(cpf_reverse[i:], start=2)
        # print(list(cpf_enumerate))
        print('dv calculado:::')

        # map pega o cpf_enumerate pega o el q é cada uma das tuplas
        # el 0: tupla 0: (2,0) multiplica 2*0,faz isso com todas as tuplas e soma o resultado
        # resultado map sem soma:
        # [0, 15, 12, 30, 6, 14, 48, 0, 80] soma = 205 * 10 = 2050 resto da div por 11 = 4
        # multiplica o resultado por 10 e pega o resto da divisão por 11 que vai dar o dig verificador FINAL CPF(49)
        # print(list(map(lambda el: int(el[1]) * el[0], cpf_enumerate)))
        # print(sum(map(lambda el: int(el[1]) * el[0], cpf_enumerate)))
        # print(205 * 10)
        # print(2050 % 11)
        dv_calculado = sum(map(lambda el: int(el[1]) * el[0], cpf_enumerate)) * 10 % 11

        print(dv_calculado)
        # IF converte para string e compara o dig verificado
        print(f"if:::")
        print(str(dv_calculado % 10))
        if cpf_reverse[i - 1 : i] != str(dv_calculado % 10):
            return False

    return True


if __name__ == "__main__":
    print(validate_cpf("80621635049"))
