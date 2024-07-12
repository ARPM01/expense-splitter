from flask import Blueprint, request, jsonify

from models.transaction import (
    get_all_transactions,
    add_transaction,
    update_transaction,
    delete_transaction,
)

transactions_bp = Blueprint("transactions", __name__)


@transactions_bp.route("/", methods=["GET"])
def get_transactions():
    transactions = get_all_transactions()
    try:
        return [__transaction_to_dict(transaction) for transaction in transactions]
    except Exception as e:
        return jsonify({"error": str(e)}), 500


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


def __transaction_to_dict(transaction):
    transaction["_id"] = str(transaction["_id"])
    return transaction
