from flask_pymongo import PyMongo
from pymongo import MongoClient

mongo = None


def init_db(app):
    global mongo
    # mongo = PyMongo(app, uri=app.config["MONGO_URI"])
    mongo = MongoClient(app.config["MONGO_URI"])
    print("connected to mongo", mongo)
