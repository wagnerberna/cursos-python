fila_id = [5, 7, 9, 15, 10]

print(fila_id[1:])

elementos = [
    {"id": id, "seguinte": id_next}
    for id, id_next in zip(fila_id, fila_id[1:] + [None])
]

print(elementos)
