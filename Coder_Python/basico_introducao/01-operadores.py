# Operadores ternários
# resposta true pega o mais prox. a esquerd., false o outro.
valida_senha = True
res_lib = "abrir cofre?" + ("Não", "Sim")[valida_senha]
print(res_lib)

# if else
valida_senha_2 = False
# leitura/escrita natural inglês
# abrir cofre sim se true senão não
res_lib_2 = "abrir cofre?" + ("Sim" if valida_senha_2 else "Não")
print(res_lib_2)

# operador Membro
# verificar se membro está presente na lista
lista3 = [1, 2, 3, "WB", "AS"]
res_lista3_num = 3 in lista3
res_lista3_str = "WB" in lista3
res_lista3_str2 = "WB" not in lista3  # negação
print(res_lista3_num, res_lista3_str, res_lista3_str2)

# operador de Identidade
x = 3
y = x
z = 3
# ambos true pois possuem o mesmo valor
comp_x_y = x is y
comp_y_z = y is z

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]
# true e false pois não apontam para o mesmo end de memória
print(lista_a is lista_b, lista_b is lista_c)
