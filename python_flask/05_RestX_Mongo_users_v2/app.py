from flask import Flask, Response, request
from flask_restx import Api, Resource
from src.controller.user import users_ns, user_add_ns, user_ns
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


api.add_namespace(users_ns, path='/')
api.add_namespace(user_add_ns, '/')
api.add_namespace(user_ns, '/')


if __name__ == '__main__':
    app.run(debug=True)
