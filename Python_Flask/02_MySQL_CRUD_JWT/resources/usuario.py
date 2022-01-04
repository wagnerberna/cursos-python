from flask_restful import Resource, reqparse
from models.usuario import UserModel

from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, jwt_required


# from werkzeug.security import safe_str_cmp:(método seguro de comparação de senha / Import nativo python)


# atributos passa a ser uma variável global:
atributos = reqparse.RequestParser()
atributos.add_argument(
    "login",
    type=str,
    required=True,
    help="The field 'login'cannot bel left blank",
)
atributos.add_argument(
    "senha",
    type=str,
    required=True,
    help="The field 'senha'cannot bel left blank",
)


class User(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument(
        "nome",
        type=str,
        required=True,
        help="The field 'nome' cannot be left blank.",
    )
    atributos.add_argument(
        "login",
        type=float,
        required=True,
        help="the field 'login' cannot bel left blank",
    )
    atributos.add_argument("nome")
    atributos.add_argument("login")

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {"message": "User not found."}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
                return {"message": "user deleted."}
            except:
                return {
                    "message": "An interna erro ocurred trying to delete user."
                }, 500
        return {"message": "user not found."}, 404


# .parse_args() salva todos atributos recebidos na variável indicada
class UserRegister(Resource):
    def post(self):
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados["login"]):
            return {"message": f"the login: {dados['login']} alredy exists."}

        user = UserModel(**dados)
        user.save_user()
        return {"message": "user created successfully"}, 201


# safe_str_cmp (método seguro de comparação de senha / Import nativo python)
class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados["login"])
        if user and safe_str_cmp(user.senha, dados["senha"]):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {"access_token": token_de_acesso}, 200
        return {"message": "The username or password is incorrect."}, 401
