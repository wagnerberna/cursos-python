# Set conjunto { } semelhante lista
# Não indexado / Não aceita repetir el.
# ordem aleatória
conjunto1 = {1, 2, 3, 3, 3}
conjunto2 = {"wagner", "Aline", "wagner"}
conjunto3 = set("wagnerrrr")
valida_a = "w" in conjunto2
valida_nome = "wagner" in conjunto2
# Não repete e a ordem é indiferente
valida_iguais = {1, 2, 3} == {3, 2, 1, 3, 2, 1}

# Operações de Conjuntos
conj4 = {1, 2}
conj5 = {2, 3}
# union
conj6 = conj4.union(conj5)
# Intersection (el. comuns aos dois conj.)
conj7 = conj4.intersection(conj5)

conj8 = {10, 11}
conj9 = {11, 12}
# update (atualiza o 1º com os do 2º)
conj8.update(conj9)

# Verificar se um conjunto é subconjunto do outro
# conj9 está contido em conj8(após update)
conj9_contido_conj8 = conj9 <= conj8
# conj8 é super conjunto do conj9
# conj8 contém conj9
conj8_contem_conj9 = conj8 >= conj9
# diferença entre conjuntos "-"
conj8_menos_el_conj8 = conj8 - conj9
# Não existe a op. "+"

# atribuir diferença ao próprio conj.
conj10 = {20, 30}
conj11 = {30, 40}
# conj10 -= conj11
dif_conj10_conj11 = conj10 - conj11
dif_conj11_conj10 = conj11 - conj10
