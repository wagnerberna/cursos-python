# import padrão do python q não dá erro de tipagem:
# from dataclasses import dataclass
# import pydantic:
from pydantic.dataclasses import dataclass
from pydantic import StrictInt, StrictStr

@dataclass
class Pessoa:
    nome: str
    idade: int

p1 = Pessoa(nome="Wagner", idade=40)
# pydantic converte o str para int sozinho:
p2 = Pessoa(nome="Wagner", idade="40")
# Erro de validação:
# p3 = Pessoa(nome="Wagner", idade="")

print(p1, p2)
# print(p3)

# strict int permite q só números inteiros sejam adicionados
@dataclass
class Pet:
    nome: StrictStr
    idade: StrictInt

pet1 = Pet(nome="Thor", idade=7)
pet2 = Pet(nome="Thor", idade="7")
print(pet1)
print(pet1.nome)
# erro de validação:
# print(pet2)




