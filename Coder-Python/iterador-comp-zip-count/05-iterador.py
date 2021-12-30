import sys

# iterador
lista = [0, 1, 2, 3, 4, 5]
print(hasattr(lista, "__iter__"))
print(hasattr(lista, "__next__"))
# for torna a lista iterável
lista = iter(lista)
print(hasattr(lista, "__iter__"))
print(hasattr(lista, "__next__"))
# print(next(lista))
# print(next(lista))
# print(next(lista))

lista1 = [el for el in range(1000)]
print(type(lista))
# () -  tranforma a lista em um gerador
lista2 = (el for el in range(1000))
print(type(lista))
print(sys.getsizeof(lista1))
print(sys.getsizeof(lista2))

# for / gerador / iterador ()
gerador = (el for el in range(6))
print(next(gerador))
print(next(gerador))
for el in gerador:
    print(el)

# Carrinho de compra somando valores
carrinho = []
carrinho.append(("Produto 1", 30.50))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 50))
total = sum([float(valor) for produto, valor in carrinho])
print(carrinho)
print(total)
