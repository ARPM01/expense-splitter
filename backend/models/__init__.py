from flask_pymongo import PyMongo
from pymongo import MongoClient

mongo = None


def init_db(app):
    global mongo
    mongo = MongoClient(app.config["MONGO_URI"])
