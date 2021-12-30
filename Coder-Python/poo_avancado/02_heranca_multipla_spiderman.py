# 1 objeto herdar multiplas classes
# classe pai
class Animal:
    @property
    def capacidades(self):
        return ("dormir", "comer", "beber")


# classe filha
# concatena capacidades da classe pai com a da filha
class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ("amar", "falar", "estudar")


# classe filha
class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ("fazer teia", "andar pelas paredes")


# classe "Neta"
# super chama as duas classes
class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + (
            "bater em bandidos",
            "atirar teias entre prédios",
        )


if __name__ == "__main__":
    john = Homem()
    print(f"John: {john.capacidades}")

    aranha = Aranha()
    print(f"Aranha: {aranha.capacidades}")

    peter = HomemAranha()
    print(f"Peter Parker: {peter.capacidades}")
