from pydantic import BaseModel, Extra, Field
from typing import Optional

# adrress está no segundo nível
# dados opcionais senão passados pegam None ou se tiver o valor default
class Address(BaseModel):
    """
    Cat API Address definition
    """

    city: str
    zip_code: Optional[str] = ""
    number: Optional[int] = 0


#  class config "Extra.forbid" proíbe campos adicionais, se forem enviados dá erro
class UserRequest(BaseModel):
    """
    Cat API Request definition
    """

    # class Config:
    #     extra = Extra.forbid

    name: str
    age: int
    address: Address


my_json = {
    "name": "Bruce",
    "age": 35,
    "address": {"city": "Gotam", "zip_code": "ABCDE", "number": 123},
}

data = UserRequest.parse_obj(my_json)
print(data)
print(data.name)
print(data.address)


my_json_2 = {
    "name": "Clark",
    "lastname": "Kent",
    "age": 30,
    "address": {"state": "NY", "city": "New York"},
}

# Pega apenas os dados definidos no contrato
data2 = UserRequest.parse_obj(my_json_2)
print(data2)
print(data2.name)
print(data2.address)
