from pydantic import BaseModel, validator
from typing import List


class Pedidos(BaseModel):
    ids: List[int]


# VER Documentação não funcionou
# prevalidador converte antes de usar
# @validator("ids", pre=True)
# def convert_ids(cls, value):
#     return value.split(",")


# ped01 = Pedidos(ids="1,2,3,4,5")
# print(ped01)

# VER Documentação não funcionou
# verifica cada um dos itens da lista
@validator("ids", each_item=True)
def check_ids(cls, value):
    if value < 0:
        raise ValueError("Ids não podem ser negativos")
    return value


ped01 = Pedidos(ids=[1, 2, -3, 4, 5])
print(ped01)
