from . import mongo


def get_all_users():
    return list(mongo.db.users.find())


def add_user(user):
    return mongo.db.users.insert_one(user)
