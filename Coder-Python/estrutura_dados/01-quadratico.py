# V1
# Quadrática for dentro de for
# FN verifica se têm item duplicado
# 1º for compara cada item da lista com todos el da lista através do 2º for
# se terminar e não encontrar duplicado retorna falso
def has_duple(lista):  # [a, b, c, d]
    for index, el in enumerate(lista):  # 0, a
        # começa no index+1 e vai até o final :
        for el_to_compare in lista[index + 1 :]:  # [b, c, d]
            if el == el_to_compare:
                return True
    return False


lista1 = ["a", "b", "c", "d"]
lista2 = ["a", "b", "a", "c", "d"]

print(has_duple(lista1))
print(has_duple(lista2))
