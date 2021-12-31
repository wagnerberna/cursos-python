# comprehension_dict {}

li_num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li_nomes = ["Wagner", "Aline", "Cris"]

li_comp_dict = [
    {el_num: el_nomes} for el_num in li_num2 for el_nomes in li_nomes
]
print(li_comp_dict)

# Converter tupla em dict alterando posições
tupla = (
    ("chave", "valor"),
    ("chave2", "valor2"),
)
conv_tuple_dict = [{el_val: el_chave} for el_chave, el_val in tupla]
print(conv_tuple_dict)
