# Atributo da classe sem usar construtor
# 1 cópia compartilhada com todas instâncias
class Humano:
    especie = "Homo Sapiens"

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    # Atributo método de Leitura
    # usa decorator
    @property
    def idade(self):
        return self._idade

    # Atributo método de Escrita
    # usa decorator p acessar como se fosse um atributo
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError("Idade deve ser positivo")
        self._idade = idade

    # método instância recebe "self"
    # return self permite encadear chamada
    def das_cavernas(self):
        self.especie = "Homo Neanderthalensis"
        return self

    # método estático S/ param.
    # decorator "@"
    @staticmethod
    def especies():
        adjetivos = ("Habilis", "Erectus", "Neanderthalensis", "Sapiens")
        return ("Australopiteco",) + tuple(f"Homo {adj}" for adj in adjetivos)
        # return f'Australopiteco, {tuple("Homo {el}"  for el in adjetivos)}'

    # método de Classe param. classe "cls"
    # decorator "@"
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


# subClasse da Humano
class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


# Classe Pai
print("Classe Pai")
jose = Humano("José")
# cesar = Humano("César")
# cesar.das_cavernas()
# ou
# cesar = Humano("César")
# Humano.das_cavernas(cesar)
# ou encadeado
cesar = Humano("César").das_cavernas()

# acesso atributo da classe humano
print(f"Humano especie:{Humano.especie}")
# acesso atributo da instâncias do objeto
print(f"Jose especie: {jose.especie}")
print(f"César especie: {cesar.especie}")
print(cesar.nome)
print(cesar.especie)

# SubClasses
print("subClasses")
#  Criando objeto através das subClasses
grundy = Neanderthal("Grundy")
print(grundy.nome)
print(grundy.especie)

grokn = Neanderthal("Grokn")
print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
print(HomoSapiens.especies())
print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')
print(f"Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}")
print(f"Neanderthal evoluído? {Neanderthal.is_evoluido()}")
print(f"José evoluído? {jose.is_evoluido()}")
print(f"Grokn evoluído? {grokn.is_evoluido()}")

# Atributos método de leitura e escrita por função get e set:
# adao = HomoSapiens("Adão")
# print(f"Nome: {adao.nome} Idade: {adao.get_idade()}")
# adao.set_idade(40)
# print(f"Nome: {adao.nome} Idade: {adao.get_idade()}")
# adao.set_idade(-40)

# Atributos método de leitura e escrita por decorator:
# igual acesso um atributo e não como se fosse função
adao = HomoSapiens("Adão")
adao.idade = 40
print(f"Nome: {adao.nome} idade: {adao.idade}")
# adao.idade = -40
