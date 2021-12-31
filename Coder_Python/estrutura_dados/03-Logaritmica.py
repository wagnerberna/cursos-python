# # V3 Refatorado Logaritmica divide a lista
def has_duple(lista):  # [a, b, c, d]
    lista.sort()  # (n * log n)
    # transforma em 2 listas:
    # 1º do inicio até penúltimo, 2ª do segundo até o último
    for el_l1, el_l2 in zip(lista[:-1], lista[1:]):  # [a b c] [b c d] # (n)
        print(el_l1, el_l2)
        if el_l1 == el_l2:
            return True
    return False


lista1 = ["a", "b", "c", "d"]
lista2 = ["a", "b", "a", "c", "d"]

print(has_duple(lista1))
print(has_duple(lista2))
