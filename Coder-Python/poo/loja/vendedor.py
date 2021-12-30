from .pessoa import Pessoa

# subClasse Vendedor
# param. Herda da Classe Pessoa
class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
