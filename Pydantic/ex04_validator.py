from pydantic import BaseModel, validator

# senha 1 e 2 campo de confirmar senha
class Cadastro(BaseModel):
    nome: str
    idade: int = 0
    email: str
    senha_1: str
    senha_2: str

    # "*" validar todos os campos
    @validator("*")
    def field_not_empty(cls, field):
        if field == "":
            raise ValueError("Campo não pode estar vazio")
        return field

    # Sintaxe do validador é um decorator com o nome do campo
    # value é o valor passado na chave email
    @validator("email")
    def email_valid(cls, value):
        if "@" not in value:
            raise ValueError("Email não têm @")
        return value

    # validar dois campos com 1 decorator
    @validator("senha_1", "senha_2")
    def password_lenght(cls, value):
        if len(value) >= 8:
            return value
        raise ValueError("Senha menor que 8")

    # Validador senhas iguais
    # values dá acesso a todos os valores dos campos
    @validator("senha_2")
    def passwords_equal(cls, value, values):
        if value == values["senha_1"]:
            return value
        raise ValueError("Senhas diferentes")


cad0 = Cadastro(
    **{
        "nome": "Barry",
        "idade": 25,
        "email": "Flash@g.com",
        "senha_1": "12345678",
        "senha_2": "12345678",
    }
)
print(cad0)
print(cad0.nome)

cad1 = Cadastro(
    **{
        "nome": "Bruce",
        "idade": 30,
        "email": "bat@g.com",
        "senha_1": "12345678",
        "senha_2": "12345678",
    }
).dict()
print(cad1)
print(cad1["nome"])

# ".json()" converte para json
# ".dict() "
cad2 = Cadastro(
    **{
        "nome": "Clark",
        "idade": 35,
        "email": "sup@g.com",
        "senha_1": "12345678",
        "senha_2": "12345678",
    }
).json()
print(cad2)

# aparece ambos todos erros: @ e senha
cad3 = Cadastro(
    **{
        "nome": "",
        "idade": 25,
        "email": "wagg.com",
        "senha_1": "1234567",
        "senha_2": "1234567",
    }
)
