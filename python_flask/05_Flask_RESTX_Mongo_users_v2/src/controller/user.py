from flask import Response, request
from flask_restx import Resource, Namespace
from src.model.user import UserModel
from bson.objectid import ObjectId
import json


users_ns = Namespace('users_get_all', description='namespace for get all users')
user_add_ns = Namespace('user_add', description='Post user add')
user_ns = Namespace('user_by_id', description='User by id find, update and delete')

# GetAll
@users_ns.route('/users')
class UsersController(Resource):
    def get(self):
        try:
            data_users = UserModel().get_all()
            print(data_users)

            if data_users == None:
                return Response(
                    response=json.dumps({'message': 'user not found', 'id': f'{id}'}),
                    status=404,
                    mimetype='application/json',
                )

            for user in data_users:
                user['_id'] = str(user['_id'])
            print('------------')
            print(data_users)
            return Response(response=json.dumps(data_users), status=200, mimetype='application/json')

        except Exception as ex:
            return Response(
                response=json.dumps({'message': 'cannot read users'}), status=500, mimetype='application/json'
            )


# Post
@user_add_ns.route('/useradd')
class UserAddController(Resource):
    def post(self):
        try:
            # # FORM
            # data = request.form
            # print(data)
            # name = data['name']
            # last_name = data['lastname']
            # new_user = {'name': name, 'last_name': last_name}
            # print(new_user)

            # JSON
            data = request.get_json()
            print(data)
            name = data.get('name')
            last_name = data.get('lastname')
            new_user = {'name': name, 'last_name': last_name}
            print(new_user)

            data_add = UserModel().add(new_user)
            # id do ítem adicionado
            id = data_add.inserted_id
            print('----')
            print(id)
            print(data_add)

            return Response(
                response=json.dumps({'message': 'user created', 'id': f'{id}'}),
                status=201,
                mimetype='application/json',
            )
        except Exception as ex:
            print(ex)
            return Response(
                response=json.dumps({'message': 'cannot create user'}), status=500, mimetype='application/json'
            )


# GetById / Update / Delete
@user_ns.route('/user/<id>')
class UserController(Resource):
    def get(self, id):
        try:
            print('----controller----')
            data_user = UserModel().get_by_id(id)
            print(data_user)

            if data_user == None:
                return Response(
                    response=json.dumps({'message': 'user not found', 'id': f'{id}'}),
                    status=404,
                    mimetype='application/json',
                )

            print('---')
            name = data_user.get('name')
            last_name = data_user.get('last_name')
            id_db = str(data_user.get('_id'))
            print(name, last_name, id_db)
            if data_user:
                return Response(
                    response=json.dumps({'name': name, 'lastname': last_name, 'id': id_db}),
                    status=200,
                    mimetype='application/json',
                )

        except Exception as ex:
            print(ex)
            return Response(
                response=json.dumps({'message': 'internal error'}), status=500, mimetype='application/json'
            )

    def put(self, id):
        try:
            # # FORM
            # data = request.form
            # print(data)
            # name = data['name']
            # last_name = data['lastname']

            # JSON
            data = request.get_json()
            print(data)
            name = data.get('name')
            last_name = data.get('lastname')
            new_user = {'name': name, 'last_name': last_name}
            print(new_user)

            print('---PUT---')
            print(name, last_name, ObjectId(id))
            data_update = UserModel().update(id, name, last_name)
            print('---Put2---')
            print(data_update)
            # verificar se foi feito o update pelo atributo de count
            print(data_update.modified_count)
            if data_update.modified_count == 1:
                return Response(
                    response=json.dumps({'message': 'user update'}), status=200, mimetype='application/json'
                )

            # else caso não tenha sido realizada alterações
            return Response(
                response=json.dumps({'message': 'nothing to update'}), status=409, mimetype='application/json'
            )

        except Exception as ex:
            print(ex)
            return Response(
                response=json.dumps({'message': 'cannot update user'}), status=500, mimetype='application/json'
            )

    def delete(self, id):
        try:
            data_delete = UserModel().delete(id)

            # attr ver atributos do objeto retornado (delete_count)
            # for attr in dir(data_delete):
            #     print(f'****{attr}****')

            if data_delete.deleted_count == 1:
                return Response(
                    response=json.dumps({'message': 'user delete', 'id': f'{id}'}),
                    status=200,
                    mimetype='application/json',
                )
            # else
            return Response(
                response=json.dumps({'message': 'user not found', 'id': f'{id}'}),
                status=404,
                mimetype='application/json',
            )

        except Exception as ex:
            print(ex)
            return Response(
                response=json.dumps({'message': 'cannot delete user'}), status=500, mimetype='application/json'
            )
