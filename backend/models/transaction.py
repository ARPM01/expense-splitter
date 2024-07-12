from bson.objectid import ObjectId
from . import mongo


def get_all_transactions():
    if mongo:
        return list(mongo.db.transactions.find())


def add_transaction(transaction):
    result = mongo.db.transactions.insert_one(transaction)
    return result.inserted_id


def update_transaction(transaction_id, transaction):
    mongo.db.transactions.update_one(
        {"_id": ObjectId(transaction_id)}, {"$set": transaction}
    )


def delete_transaction(transaction_id):
    mongo.db.transactions.delete_one({"_id": ObjectId(transaction_id)})
