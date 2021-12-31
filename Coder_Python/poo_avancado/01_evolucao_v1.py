# Atributo da classe sem usar construtor
# 1 cópia compartilhada com todas instâncias
class Humano:
    especie = "Homo Sapiens"

    def __init__(self, nome):
        self.nome = nome

    # return self permite encadear chamada
    def das_cavernas(self):
        self.especie = "Homo Neanderthalensis"
        return self


jose = Humano("José")
# cesar = Humano("César")
# cesar.das_cavernas()
# ou
# cesar = Humano("César")
# Humano.das_cavernas(cesar)
# ou encadeado
cesar = Humano("César").das_cavernas()
# ou

# acesso atributo da classe humano
print(f"Humano especie:{Humano.especie}")
# acesso atributo da instâncias do objeto
print(f"Jose especie: {jose.especie}")
print(f"César especie: {cesar.especie}")
