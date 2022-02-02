from flask import Flask, Response, request
from flask_restx import Api, Resource
import pymongo
import json

# import permite usar o id como text
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

# conexão com o Mongo pelo pymongo
try:
    mongo = pymongo.MongoClient(host='localhost', port=27017, serverSelectionTimeoutMS=1000)
    db = mongo.dcheroes
    mongo.server_info()  # trigger exception if cannot connect to db
except:
    print('ERROR - Cannot connect to db')

# getAll
@api.route('/users')
class users(Resource):
    def get(self):
        try:
            data = list(db.users.find())
            print(data)
            print('--------')
            # str converte o objetc id(direita) em string 'text id' (esquerda)
            for user in data:
                user['_id'] = str(user['_id'])
            print('--------')
            print(data)
            return Response(response=json.dumps(data), status=200, mimetype='application/json')

        except Exception as ex:
            return Response(
                response=json.dumps({'message': 'cannot read users'}), status=500, mimetype='application/json'
            )


# Post
@api.route('/useradd')
class userAdd(Resource):
    def post(self):
        try:
            name = request.form['name']
            last_name = request.form['lastname']
            new_user = {'name': name, 'last_name': last_name}
            print(new_user)

            # database.collection
            dbResponse = db.users.insert_one(new_user)
            id = dbResponse.inserted_id
            # print(id)

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
@api.route('/user/<id>')
class userResource(Resource):
    def get(self, id):
        try:
            dbResponse = db.users.find_one({'_id': ObjectId(id)})
            print(dbResponse)
            print('---')
            name = dbResponse.get('name')
            last_name = dbResponse.get('last_name')
            id_db = str(dbResponse.get('_id'))
            print(name, last_name, id_db)
            if dbResponse:
                return Response(
                    response=json.dumps({'name': name, 'lastname': last_name, 'id': id_db}),
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
                response=json.dumps({'message': 'internal error'}), status=500, mimetype='application/json'
            )

    # ObjectId converter id
    def put(self, id):
        try:
            name = request.form['name']
            last_name = request.form['lastname']
            print('---PUT---')
            print(name, last_name)
            dbResponse = db.users.update_one(
                {'_id': ObjectId(id)}, {'$set': {'name': name}}, {'$set': {'last_name': last_name}}
            )

            # verificar se foi feito o update pelo atributo de count
            print(dbResponse.modified_count)
            if dbResponse.modified_count == 1:
                return Response(
                    response=json.dumps({'message': 'user update'}), status=200, mimetype='application/json'
                )

            # else caso não tenha sido realizada alterações
            return Response(
                response=json.dumps({'message': 'nothing to update'}), status=200, mimetype='application/json'
            )

        except Exception as ex:
            print(ex)
            return Response(
                response=json.dumps({'message': 'cannot update user'}), status=500, mimetype='application/json'
            )

    def delete(self, id):
        try:
            dbResponse = db.users.delete_one({'_id': ObjectId(id)})

            # attr ver atributos (delete_count)
            # for attr in dir(dbResponse):
            #     print(f'****{attr}****')

            if dbResponse.deleted_count == 1:
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


if __name__ == '__main__':
    app.run(debug=True)
