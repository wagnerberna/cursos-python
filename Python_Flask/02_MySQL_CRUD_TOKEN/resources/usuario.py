from flask_restful import Resource, reqparse
from models.usuario import UserModel


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
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados["login"]):
            return {"message": f"the login: {dados['login']} alredy exists."}

        user = UserModel(**dados)
        user.save_user()
        return {"message": "user created successfully"}, 201
