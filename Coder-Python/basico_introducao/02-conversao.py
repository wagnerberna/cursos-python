# Conversões
a = 2
b = "3"
c = "3.2"
d = 4
e = 5.1
valid_int = e.is_integer()

print(type(a), type(b))
# p
convert_inteiro = a + int(b)

convert_string = str(a) + b

convert_float = a + float(c)

divisao_gera_float = d / a

divisao_gera_int = d // a

# true 1 / false 0
soma_true = 2 + True
soma_false = 2 + False

print(dir(int))

# STRING \n quebra linha \t tab
meu_nome = "Wagner Berna"
tamanho_nome = len(meu_nome)
nome_upper_case = meu_nome.upper()
nome_lower_case = meu_nome.lower()

letra1 = meu_nome[-1]
# acessar um conjunto (range) de el começando no 2 inclui o 2
letras2 = meu_nome[2:]
letras3 = meu_nome[-5:]
# acessar um conjunto (range) de el até o 3 Não inclui o 3
letras3 = meu_nome[:3]
# acessar um conjunto (range) inicio e fim
letras4 = meu_nome[3:6]
# acessar um conjunto (range) pulando 1 el (x:x:2)
letras5 = meu_nome[1:10:2]
# Inverter string
nome_invertido = meu_nome[::-1]

texto_aspas = "bla bla 'blo' bla"
texto_multiplas_linhas = """ bla bla
\t ... bla bla bla """
print(texto_multiplas_linhas)

# split segmenta como padrão pelo espaços
texto_segmentado = texto_aspas.split()
# altereando separador q não inclui no res
texto_segmentado2 = texto_aspas.split("l")

# operador Membro (diferencia maiúscula)
blo_existe_no_texto = "blo" in texto_aspas

# Métodos mágicos
