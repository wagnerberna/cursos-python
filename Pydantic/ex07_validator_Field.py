from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from decimal import Decimal
from datetime import datetime

# https://pydantic-docs.helpmanual.io/usage/schema/

# idade têm de ser maior q 17, valor padrão 18
# valor maior q 1 real
# data valor defalut data atual
class Cadastro(BaseModel):
    nome: str
    idade: int = Field(int(18), gt=17)
    email: EmailStr
    valor_pedido: Decimal = Field(gt=1.0)
    date_create: datetime = Field(default_factory=datetime.now)


cad1 = Cadastro(
    **{
        "nome": "Bruce",
        "email": "bat@g.com",
        "valor_pedido": 5.5,
        "date_create": "2020-01-29T05:20:30",
    }
)
print(cad1)
print(cad1.valor_pedido)

cad2 = Cadastro(
    **{
        "nome": "Bruce",
        "email": "bat@g.com",
        "valor_pedido": 5.5,
    }
)
print(cad2)
print(cad2.date_create)
