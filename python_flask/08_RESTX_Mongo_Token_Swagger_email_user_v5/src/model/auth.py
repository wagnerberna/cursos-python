from src.service.mongo import Mongo
from bson.objectid import ObjectId

db = Mongo().mongo_connect()


class AuthModel:
    def find_login(self, login):
        find_user = db.users.find_one({'login': login})
        if find_user:
            return find_user
        return None