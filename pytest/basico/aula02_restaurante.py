#  se o valor de pedidos na fila for maior ou igual 0: add valor
# senão gera erro
class Restaurante:
    def __init__(self, nome, pedidos_na_fila=0):
        self.nome = nome
        if pedidos_na_fila >= 0:
            self.pedidos_na_fila = pedidos_na_fila
        else:
            raise ValueError("a quant. de pedidos deve ser maior que zero")

    def adiciona_pedido(self):
        self.pedidos_na_fila += 1

    def remove_pedido(self):
        if self.pedidos_na_fila > 0:
            self.pedidos_na_fila -= 1
