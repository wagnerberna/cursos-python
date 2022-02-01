# Criação da classe
class Data:
    # criar método "FN" dentro da classe
    def to_str(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


# instanciar um novo objeto
d1 = Data()
# criar atributos / valores
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(f"{d1.dia}/{d1.mes}/{d1.ano}")
print(d1.to_str())

d2 = Data()
# criar atributos / valores
d2.dia = 7
d2.mes = 10
d2.ano = 2021
print(d2.to_str())
