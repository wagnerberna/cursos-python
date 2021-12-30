compras = (
    {"quantidade": 2, "preco": 10},
    {"quantidade": 3, "preco": 20},
    {"quantidade": 5, "preco": 14},
)

totais = tuple(map(lambda el: el["quantidade"] * el["preco"], compras))

print(f"preços Totais: {totais}")
print(f"Total geral:{sum(totais)}")
