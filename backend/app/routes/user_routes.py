from controller.user_controller import user_controller
from flask import Blueprint, request, jsonify

user_routes = Blueprint('user_routes', __name__)
def userRoutes(app):
    @user_routes.route("/user/register", method=["POST"])
    def register():
        data = request.json
        return user_controller.register(data)
    
    @user_routes.route("/user/login", method=["POST"])
    def login():
        data = request.json
        return user_controller.login(data)
    
    @user_routes.route("/user/query_user_by_name", method=["GET"])
    def query_user_by_name():
        data = request.json
        return user_controller.query_user_by_name(data)
    
    @user_routes.route("/user/update_user_detail", method=["POST"])
    def update_user_detail():
        data = request.json
        return user_controller.update_user_detail(data)
    
    @user_routes.route("/user/delete_user", method=["POST"])
    def delete_user():
        data = request.json
        return user_controller.delete_user(data)
