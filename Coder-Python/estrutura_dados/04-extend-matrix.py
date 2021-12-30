lista1 = [1, 2, 3]
palavra = "abc"
lista1.extend(palavra)
print(lista1)


# matrix
# [[1,2],
#  [3,4]]

lista = [[1, 2], [3, 4]]


def matrix_reshape(matrix):
    print(matrix)
    # número de linhas = total de elementos
    rows = len(matrix)
    # número de colunoas = quant. de itens no el.
    columns = len(matrix[0])
    print(rows, columns)
    # transforma a matrix em uma linha
    # retira dos arrays internos
    line = []
    for row in matrix:
        line.extend(row)
    print(line)


print(matrix_reshape(lista))
