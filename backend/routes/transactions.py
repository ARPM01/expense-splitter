from flask import Blueprint, request, jsonify
from models.transaction import (
    get_all_transactions,
    add_transaction,
    update_transaction,
    delete_transaction,
)
from flask_cors import CORS

transactions_bp = Blueprint("transactions", __name__)


@transactions_bp.route("/", methods=["GET"])
def get_transactions():
    transactions = get_all_transactions()
    print(transactions, type(transactions))
    return jsonify(transactions)


@transactions_bp.route("/", methods=["POST"])
def create_transaction():
    data = request.json
    transaction_id = add_transaction(data)
    return jsonify({"status": "Transaction added", "id": str(transaction_id)}), 201


@transactions_bp.route("/<transaction_id>", methods=["PUT"])
def modify_transaction(transaction_id):
    data = request.json
    update_transaction(transaction_id, data)
    return jsonify({"status": "Transaction updated"}), 200


@transactions_bp.route("/<transaction_id>", methods=["DELETE"])
def remove_transaction(transaction_id):
    delete_transaction(transaction_id)
    return jsonify({"status": "Transaction deleted"}), 200
