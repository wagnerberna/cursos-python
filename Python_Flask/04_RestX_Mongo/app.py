from flask import Flask, Response, request
from flask_restx import Api, Resource
import pymongo
import json

# import permite usar o id como text
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

try:
    mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS=1000)
    db = mongo.unicred
    mongo.server_info()  # trigger exception if cannot connect to db
except:
    print('ERROR - Cannot connect to db')


@api.route('/users')
class users(Resource):
    def get(self):
        try:
            data = list(db.users.find())
            print(data)
            # str converte o objetc id(direita) em string "text id" (esquerda)
            for user in data:
                user['_id'] = str(user['_id'])
            print('--------')
            print(data)
            return Response(response=json.dumps(data), status=200, mimetype='application/json')

        except Exception as ex:
            return Response(
                response=json.dumps({'message': 'cannot read users'}), status=500, mimetype='application/json'
            )


@api.route('/useradd')
class userAdd(Resource):
    def post(self):
        try:
            name = request.form['name']
            last_name = request.form['lastname']
            new_user = {
                'name': name,
                'last_name': last_name,
            }
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
            return Response(
                response=json.dumps({'message': 'cannot create user'}), status=500, mimetype='application/json'
            )


@api.route('/user<int:id>')
class userResource(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


if __name__ == '__main__':
    app.run(debug=True)
