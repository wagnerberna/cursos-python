compras = (
    {"quantidade": 2, "preco": 10},
    {"quantidade": 3, "preco": 20},
    {"quantidade": 5, "preco": 14},
)


def calc_preco_total(el):
    return el["quantidade"] * el["preco"]


totais = tuple(map(calc_preco_total, compras))

print(f"preços Totais: {totais}")
print(f"Total geral:{sum(totais)}")
