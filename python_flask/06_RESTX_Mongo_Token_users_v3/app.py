from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from src.controller.user import users_ns
from src.controller.auth import auth_ns


app = Flask(__name__)
# config Token
app.config["JWT_SECRET_KEY"] = "Udemy"
# app.config["JWT_BLACKLIST_ENABLED"] = True

api = Api(app)
jwt = JWTManager(app)

api.add_namespace(users_ns, path='/')
api.add_namespace(auth_ns, path='/')


if __name__ == '__main__':
    app.run(debug=True)
