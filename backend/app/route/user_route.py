from controller.user_controller import user_controller
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

user_routes = Blueprint('user_routes', __name__)
# def userRoutes(app):
@user_routes.route("/user/register", methods=["POST"])
def register():
    data = request.get_json()
    print(data)
    return user_controller.register(data)

@user_routes.route("/user/login", methods=["POST"])
def login():
    data = request.get_json()
    return user_controller.login(data)

@user_routes.route("/user/query_user_by_name", methods=["GET"])
@jwt_required()
def query_user_by_name():
    current_user = get_jwt_identity()
    data = request.get_json()
    return user_controller.query_user_by_name(data)

@user_routes.route("/user/update_user_detail", methods=["POST"])
@jwt_required()
def update_user_detail():
    current_user = get_jwt_identity()
    data = request.get_json()
    return user_controller.update_user_detail(data)

@user_routes.route("/user/delete_user", methods=["POST"])
@jwt_required()
def delete_user():
    current_user = get_jwt_identity()
    data = request.get_json()
    return user_controller.delete_user(data)

@user_routes.route("/user/get_user_name_ids", methods=["GET"])
@jwt_required()
def get_user_name_ids():
    #the ids argument should be set type
    data = request.get_json()
    return user_controller.get_user_names_by_ids(data)

@user_routes.route("/user/increase_credits", methods=["POST"])
def increase_credits():
    data = request.get_json()
    return user_controller.increse_credit(data)

@user_routes.route("/user/query_credit_by_user", methods=["GET"])
def query_credit_by_user():
    data = request.get_json()
    return user_controller.query_credit_by_user(data)