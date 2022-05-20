from flask import Response, request
from flask_restx import Resource
# from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required
from src.model.user import UserModel
from src.service.payload.user import users_ns, user_post_put_fields, token_header
from src.service.message import *


# GetAll
@users_ns.route('users')
class UsersController(Resource):
    def get(self):
        try:
            data_users = UserModel().get_all()

            if data_users == None:
                return NOT_FOUND, 404
            
            # converte todos ids da lista em string
            for user in data_users:
                user['_id'] = str(user['_id'])
                # del user['password']
            return data_users, 200

        except:
            return INTERNAL_ERROR, 500


# Post
@users_ns.route('useradd')
class UserAddController(Resource):
    @users_ns.expect(user_post_put_fields)
    def post(self):
        try:
            # # FORM
            # data = request.form
            # print(data)
            # name = data['name']
            # lastname = data['lastname']
            # new_user = {'name': name, 'lastname': last_name}
            # print(new_user)

            # JSON
            new_user = request.get_json()
            print(new_user)
            user_add = UserModel().add(new_user)
            # id do ítem adicionado
            id = user_add.inserted_id
            print(id)
            return {'message': 'user created', 'id': f'{id}'}, 201

        except:
            return INTERNAL_ERROR, 500


# GetById / Update / Delete
@users_ns.route('user/<id>')
class UserController(Resource):
    def get(self, id):
        try:
            data_user = UserModel().get_by_id(id)
            print(data_user)

            if data_user == None:
                return NOT_FOUND, 404
            
            name = data_user.get('name')
            last_name = data_user.get('lastname')
            id_db = str(data_user.get('_id'))
            print('---')
            print(name, last_name, id_db)
            if data_user:
                return {'name': name, 'lastname': last_name, 'id': id_db}, 200

        except:
            return INTERNAL_ERROR, 500

    @users_ns.expect(token_header, user_post_put_fields)
    @jwt_required()
    def put(self, id):
        try:
            data = request.get_json()
            data_update = UserModel().update(id, **data)

            print(request.headers)

            # verificar se foi feito o update pelo atributo de count
            print(data_update.modified_count)
            if data_update.modified_count == 1:
                return UPDATE_SUCCESS, 200
            return NOTHING_UPDATE, 409

        except:
            return INTERNAL_ERROR, 500

    @jwt_required()
    def delete(self, id):
        try:
            data_delete = UserModel().delete(id)

            if data_delete.deleted_count == 1:
                return {'message': 'user delete', 'id': f'{id}'}, 200
            return NOT_FOUND, 404

        except:
            return INTERNAL_ERROR, 500
