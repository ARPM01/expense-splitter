from flask import Blueprint, request, jsonify
from models.user import get_all_users, add_user, update_user, delete_user

users_bp = Blueprint("users", __name__, url_prefix="/api/users")


@users_bp.route("/", methods=["GET"])
def get_users():
    users = get_all_users()
    return jsonify(users)


@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    user_id = add_user(data)
    return jsonify({"status": "User added", "id": str(user_id)}), 201


@users_bp.route("/<user_id>", methods=["PUT"])
def modify_user(user_id):
    data = request.json
    update_user(user_id, data)
    return jsonify({"status": "User updated"}), 200


@users_bp.route("/<user_id>", methods=["DELETE"])
def remove_user(user_id):
    delete_user(user_id)
    return jsonify({"status": "User deleted"}), 200
