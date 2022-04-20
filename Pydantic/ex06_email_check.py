from pydantic import BaseModel, EmailStr

# necessário instalar
# pip intall email-validator


class Cadastro(BaseModel):
    nome: str
    idade: int = 0
    email: EmailStr


cad1 = Cadastro(
    **{
        "nome": "Bruce",
        "idade": 30,
        "email": "batg.com",
    }
).dict()
print(cad1)
