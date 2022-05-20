import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))


class Mongo:
    def mongo_connect(self):
        try:
            # print(MONGO_HOST, MONGO_PORT)
            mongo = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT, serverSelectionTimeoutMS=1000)
            db = mongo.dcheroes
            mongo.server_info()  # trigger exception if cannot connect to db
            return db
        except:
            print('ERROR - Cannot connect to db')
