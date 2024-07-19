from bson.objectid import ObjectId
from . import mongo


def get_all_users():
    users = mongo.db.users.find()
    return [user_to_dict(user) for user in users]


def add_user(user):
    result = mongo.db.users.insert_one(user)
    return result.inserted_id


def update_user(user_id, user):
    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user})


def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})


def user_to_dict(user):
    user["_id"] = str(user["_id"])
    return user


def get_user_by_id(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return user if user else None
