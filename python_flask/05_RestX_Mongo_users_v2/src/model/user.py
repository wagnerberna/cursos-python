from flask import Response, request
from flask_restx import Resource, Namespace
import pymongo
import json
# import permite usar o id como text
from bson.objectid import ObjectId

# conexão com o Mongo pelo pymongo
try:
    mongo = pymongo.MongoClient(host='localhost', port=27017, serverSelectionTimeoutMS=1000)
    db = mongo.dcheroes
    mongo.server_info()  # trigger exception if cannot connect to db
except:
    print('ERROR - Cannot connect to db')


# class UserModel:
#     def get_All(self, id):
