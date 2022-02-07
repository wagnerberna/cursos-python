import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")

class Mongo:
    def mongo_connect(self):
        try:
            mongo = pymongo.MongoClient(host='localhost', port=27017, serverSelectionTimeoutMS=1000)
            db = mongo.dcheroes
            mongo.server_info()  # trigger exception if cannot connect to db
            return db
        except:
            print('ERROR - Cannot connect to db')
