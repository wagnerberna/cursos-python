from urllib import response
from flask import Response, request
from flask_restx import Resource, Namespace
from flask_jwt_extended import create_access_token, jwt_required

from flask_jwt_extended.utils import get_jwt
from blacklist import BLACKLIST
from werkzeug.security import safe_str_cmp
from src.model.auth import AuthModel
from src.service.payload.auth import auth_ns, token_header, auth_login_fields
from src.service.message import *


# instanciar authmodel
auth_model = AuthModel()


# Login
@auth_ns.route('login')
@auth_ns.expect(auth_login_fields)
class LoginController(Resource):
    def post(self):
        data = request.get_json()
        login = data.get('login')
        password = data.get('password')

        find_user = auth_model.find_login(login)
        print(find_user)

        # se existir um user e a senha for igual
        # safe método seguro de comparar string de password
        # token gerado baseado no login
        if find_user != None and safe_str_cmp(find_user['password'], password):
            id = str(find_user.get('_id'))
            token = create_access_token(identity=id)
            return {'token': token}, 200

        return AUTH_FAILED, 404

# Logout
# jti (JWT Token Identifier - identificado do token (id))
@auth_ns.route('logout')
@auth_ns.expect(token_header)
class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return LOGGED_SUCCESSFUL, 200
