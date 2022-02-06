from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from src.controller.user import users_ns
from src.controller.auth import auth_ns
from src.service.message import *
from blacklist import BLACKLIST

# from src.service.check_token import verifify_blacklist, token_access_revoked

app = Flask(__name__)
# config Token
app.config["JWT_SECRET_KEY"] = "Udemy"
app.config["JWT_BLACKLIST_ENABLED"] = True

api = Api(app)
jwt = JWTManager(app)

# Verifica se o token está na blacklist
# True segue para @.revoked
@jwt.token_in_blocklist_loader
def verifify_blacklist(self, token):
    print("Teste PONTO1 VERIFICA BLACKLIST")
    print(BLACKLIST)
    print(token)
    print(token["jti"] in BLACKLIST)
    return token["jti"] in BLACKLIST

# se estiver invalidado retorna esta mensagem
@jwt.revoked_token_loader
def token_access_revoked(self, token):
    print("Teste PONTO2 TOKEN INVALIDADO")
    print(BLACKLIST)
    return LOGGED_OUT, 401



api.add_namespace(users_ns, path='/')
api.add_namespace(auth_ns, path='/')


if __name__ == '__main__':
    app.run(debug=True)
