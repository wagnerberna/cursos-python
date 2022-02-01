# # V2 Refatorado Linear
def has_duple(lista):  # [a, b, c, d]
    for index, el in enumerate(lista):  # 0, a
        # el está em lista até o final
        if el in lista[index + 1 :]:
            return True
    return False


lista1 = ["a", "b", "c", "d"]
lista2 = ["a", "b", "a", "c", "d"]

print(has_duple(lista1))
print(has_duple(lista2))
