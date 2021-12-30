# comprehension []
# expressão extendida

# gerando uma lista igual
li_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li_comp1 = [el for el in li_num]
# [expressão + for item in list]
li_comp2 = [el * 2 for el in li_num]
print(li_comp1)
# print(li_comp2)

# 2 for 2 listas
# gera tupla de el lista + el range de 0 até 2
li_comp_tuple = [
    (el_li, el_range) for el_li in li_num for el_range in range(3)
]
print(li_comp_tuple)

li_num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li_nomes = ["Wagner", "Aline", "Cris"]

# replace substituir valores
li_replace = [el.replace("a", "@").upper() for el in li_nomes]
print(li_replace)

# [expressão + for item in list + condição]
# números pares
lista = list(range(100))
num_par = [el for el in lista if el % 2 == 0]
print(num_par)

# [expressão + for item in list + condição1 + condição2]
# números pares e divisíveis por 10
num_par_div10 = [el for el in lista if el % 2 == 0 if el % 10 == 0]
print(num_par_div10)

# [el + condição1 + condição2 + else + for item in list  ]
# números pares e divisíveis por 10 senão for nenhum add 0
num_par_div10_2 = [el if el % 2 == 0 and el % 10 == 0 else 0 for el in lista]
print(num_par_div10_2)
