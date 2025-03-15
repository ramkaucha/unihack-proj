from controller.user_controller import user_controller
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

user_routes = Blueprint('user_routes', __name__)
def userRoutes(app):
    @user_routes.route("/user/register", method=["POST"])
    def register():
        data = request.get_json()
        return user_controller.register(data)
    
    @user_routes.route("/user/login", method=["POST"])
    def login():
        data = request.get_json()
        return user_controller.login(data)
    
    @user_routes.route("/user/query_user_by_name", method=["GET"])
    @jwt_required
    def query_user_by_name():
        current_user = get_jwt_identity()
        data = request.get_json()
        return user_controller.query_user_by_name(data)
    
    @user_routes.route("/user/update_user_detail", method=["POST"])
    @jwt_required
    def update_user_detail():
        current_user = get_jwt_identity()
        data = request.get_json()
        return user_controller.update_user_detail(data)
    
    @user_routes.route("/user/delete_user", method=["POST"])
    @jwt_required
    def delete_user():
        current_user = get_jwt_identity()
        data = request.get_json()
        return user_controller.delete_user(data)
