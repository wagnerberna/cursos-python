# Comentário
"""
Comentário várias linhas!
"""
# importação / dir (mostra o escopo global da memória)
import math

print(dir())
print("nome do modulo:", __name__)
print(dir(math))

texto = "resultado da soma" + 3 * ":"
n1 = 4
n2 = 3
soma = n1 + n2
print(texto, soma)
soma += 7
print("soma + 7: {}".format(soma))
soma -= 7
soma *= soma
print("soma-7, {}:{}".format("multiplicado soma", soma))

divisao = n2 // n1
print(divisao)

positive = True
negative = 3.5 == 2

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

lista.append(soma)
print("add soma")
print(lista)
lista.remove(soma)
print("remove 7")
print(lista)
print("1º el")
print(lista[0])
print("último el")
print(lista[-1])
print("número index do el 5")
print(lista.index(5))

print("junta as duas listas")
lista.extend(lista2)
print(lista)

dicionario = {"nome": "Wagner", "idade": 40}
print(dicionario)
print(dicionario["nome"])

del dicionario["idade"]
print("deletada idade")
print(dicionario)
