from flask import Flask, Response, request
from flask_restx import Api, Resource
from src.controller.user import users_ns, user_add_ns, user_ns

# import permite usar o id como text
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

api.add_namespace(users_ns, path='/')
api.add_namespace(user_add_ns, '/')
api.add_namespace(user_ns, '/')


if __name__ == '__main__':
    app.run(debug=True)
