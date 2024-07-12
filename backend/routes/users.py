from flask import Blueprint, request, jsonify
from models.user import get_all_users, add_user
from flask_cors import CORS

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["GET"])
def get_users():
    users = get_all_users()
    return jsonify(users)


@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    add_user(data)
    return jsonify({"status": "User added"}), 201
