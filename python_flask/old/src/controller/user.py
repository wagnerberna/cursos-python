from flask import Response, request
from flask_restx import Resource
import json

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