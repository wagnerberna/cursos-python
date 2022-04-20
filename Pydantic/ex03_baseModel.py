from pydantic import BaseModel
from typing import List

# Todos herdam do BaseModel são subclasses dele
# "=" passa valor padrão
class Pessoa(BaseModel):
    nome: str
    idade: int = 0


# "**" atribui direto chave valor
p1 = Pessoa(nome="Wagner", idade=40)
print(p1)

p2 = Pessoa(**{"nome": "Aline", "idade": 20})
print(p2)

# Pessoas é uma lista de pessoa
class Pessoas(BaseModel):
    pessoas: List[Pessoa]


l1 = [
    {"nome": "Bruce", "idade": 30},
    {"nome": "Clark", "idade": 25},
    {"nome": "Jonh"},
]

ps1 = Pessoas(pessoas=l1)
print(ps1)
print(ps1.pessoas[0])
