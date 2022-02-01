# import json
from flask import Flask, jsonify
from flask_restful import Api
from blacklist import BLACKLIST
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager

# JWTManager Gerenciador do JWT E autenticação
# atribui ao jwt e passa a apicação para ele
# JWT_SECRET_KEY chave do token
# habilita a blacklist do arquivo blaclist.py
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "udemy"
app.config["JWT_BLACKLIST_ENABLED"] = True
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def cria_banco():
    banco.create_all()


# verfica se o token está na blacklist se estiver retorna o id do token
@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    # print("Teste PONTO1 VERIFICA BLACKLIST")
    # print(BLACKLIST)
    print(token)
    return token["jti"] in BLACKLIST


# json.dumps converte dict para json import do json
# jsonify converte de dict para json import do flask
# 401 não autorizado
@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    # print("Teste PONTO2 TOKEN INVALIDADO")
    return jsonify({"message": "You have been logged out."}), 401


api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hoteis/<string:hotel_id>")
api.add_resource(User, "/usuarios/<int:user_id>")
api.add_resource(UserRegister, "/cadastro")
api.add_resource(UserLogin, "/login")
api.add_resource(UserLogout, "/logout")


if __name__ == "__main__":
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)
