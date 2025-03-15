#queryUserDetail
#addUser
#deleteUser
#updateUserDetail
from flask import jsonify
from model.User import User
from PassUtil import
class UserService:
    def __init__(self):
        self.user_model = User()

    def register(user: User):
        if user is None or user.userId is None:
            return jsonify({"message:": "invalid user"})
        if Pass
            user.password

    def queryUserDetail(id: int):
        if id == None or id == 0:
            return jsonify({"message:": "invalid user"})
        user = User.query.get(id)
        if user == None:
            return jsonify({"message:": "the user does not exist"})
        else:
            return jsonify({"message:": "success", "name": user.userName, "email": user.mail, "credits": user.credit})