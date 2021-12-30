from datetime import datetime
from loja import Cliente, Vendedor, Compra


def main():
    # criar instâncias do objeto com dados
    cliente = Cliente("Regina Silva", 40)
    vendedor = Vendedor("Rolando Lero", 20, 3000)
    compra1 = Compra(cliente, datetime.now(), 100)
    compra2 = Compra(cliente, datetime(2018, 10, 25), 200)
    # chamar métodos
    cliente.registrar_compras(compra1)
    cliente.registrar_compras(compra2)
    print(f"Cliente:{cliente}", "(adulto)" if cliente.is_adulto() else "")
    print(f"Vendedor: {vendedor}")

    valor_total = cliente.total_compras()
    qtde_compras = len(cliente.compras)
    print(f"Total: {valor_total} em {qtde_compras} compras")
    print(f"última compra: {cliente.get_data_ultima_compra()}")


main()
