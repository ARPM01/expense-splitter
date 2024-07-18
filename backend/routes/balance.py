from flask import Blueprint, jsonify
from models.transaction import get_all_transactions
from models.user import get_all_users
from services.calculation import calculate_balances

balance_bp = Blueprint("balance", __name__)


@balance_bp.route("/", methods=["GET"])
def get_balance():
    transactions = get_all_transactions()
    users = get_all_users()
    balances = calculate_balances(transactions, users)
    return jsonify(balances)
