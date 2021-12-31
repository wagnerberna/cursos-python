# .import relativo apartir da pasta atual
from .pessoa import Pessoa

# FN para retornar data da compra
def get_data(compra):
    return compra.data


# subClasse Cliente
# param. Herda da Classe Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    # add compras
    def registrar_compras(self, compra):
        self.compras.append(compra)

    # sem data retorna None, senão ordena lista e retorna a última -1
    # key chave de ordenação FN get_data
    def get_data_ultima_compra(self):
        return (
            None
            if not self.compras
            else sorted(self.compras, key=get_data)[-1].data
        )

    # calcula o total das compras
    def total_compras(self):
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total
