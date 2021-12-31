MAIOR_IDADE = 18


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Conversor para string
    # se idade não setada retorna só o nome
    def __str__(self):
        if not self.idade:
            return self.nome
        return f"{self.nome} ({self.idade} anos)"

    # verifica se é adulto
    # ou 0 caso idade não esteja definida
    def is_adulto(self):
        return (self.idade or 0) > MAIOR_IDADE
