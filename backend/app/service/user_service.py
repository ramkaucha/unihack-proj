from datetime import datetime
from flask import jsonify
# from backend import properties
# import backend.app.properties as properties
import properties
from model import db, User
# from ..model import db, User
from util import PassUtil
import jwt

JWT_KEY = properties.jwt_secret_key


class UserService:
    def __init__(self):
        self.user_model = User()

    def register(user: User):
        # test if the user has been exixted
        existing_user = User.query.filter_by(email=user.email).first()
        if existing_user:
            return jsonify({"message:": "the user has been existed"}), 404

        if user is None:
            return jsonify({"message:": "invalid user info input"})
        if user.user_name is None:
            return jsonify({"message:": "you must set your user name"})
        if user.password is None:
            return jsonify({"message:": "you must set your password"})
        if user.email in None:
            return jsonify({"message:": "you must set your email"})

        hash_pw = PassUtil.encrypt_password(user.password)
        new_user = User(userName=user.user_name, password=hash_pw, email=user.email, credit=0, isNew=True,
                        isDelete=False)
        db.session.add(new_user)
        db.session.commit()

    def login(userName, password):
        if userName or password is None:
            return jsonify({"message:": "the user name or the password is null"})
        user = User.query.filter_by(userName=userName).first()
        if user:
            if PassUtil.verify_password(password, user.password):
                # if all pass, teh jwt token will be produced
                payload = {
                    "userId": user.user_id,
                    "email": user.email,
                    "expires_delta": datetime.timedelta(minutes=30)
                }
                token = jwt.encode(payload, JWT_KEY, algorithm='HS256')
                print(token)
                return jsonify({"message:": "login successful"}), 200
            else:
                return jsonify({"message:": "login fail"})
        else:
            return jsonify({"message:": "the user doesn't exist"}), 404

    # filter that if the user which has not been deleted
    # need to change
    def query_user_by_name(name: str):
        if name == None:
            return jsonify({"message:": "please enter the user name"}), 404
        user = User.query.filter_by(userName=name, isDelete=False).first()

        if user == None:
            return jsonify({"message:": "the user does not exist"}), 404
        else:
            return jsonify({"message:": "success", "userId": user.user_id, "name": user.user_name, "email": user.mail,
                            "credits": user.credit, "isNew": user.is_new, "isDelete": user.is_delete}), 200

    def update_user_detail(id: int, name: str, email: str, password: str, profile: str):
        user = User.query.filter_by(userId=id, isDelete=False).first()
        if user is None:
            return jsonify({"message:": "user doesn't exists"}), 404

        if name:
            user.user_name = name
        if email:
            user.email = email
        if password:
            hash_pw = PassUtil.encrypt_password(password)
            user.password = hash_pw
        if profile:
            user.profile = profile
        try:
            db.commit()
            return jsonify({"message:": "success", "name": user.user_name, "email": user.mail}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "update failed", "error": str(e)}), 500

    def delete_user(id: int, isDelete: bool):
        user = User.query.filter_by(id, isDelete=False).first()
        if not user:
            return jsonify({"message:": "the user doesn't exist"}), 404
        if isDelete:
            user.is_delete = True
        try:
            db.commit()
            return jsonify({"message:": "delete success", "name": user.user_name, "email": user.mail}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "delete failed", "error": str(e)}), 500

    # get user by id
    @staticmethod
    def get_user_by_id(user_id: int):
        user = User.query.filter_by(user_id=user_id, isDelete=False).first()
        if user is None:
            return {"message": "user does not exist"}
        return user

    # get users by id
    @staticmethod
    def get_users_by_id(user_ids: set):
        users = User.query.filter(User.user_id.in_(user_ids), isDelete=False).all()
        return users

    # get multiple usernames by ids
    @staticmethod
    def get_user_names_by_ids(user_ids: set):
        users = UserService.get_users_by_id(user_ids)
        return {user.user_id: user.user_name for user in users}

    # increase user credit
    @staticmethod
    def increase_credit(user_id: int, amount: int):
        user = User.query.filter_by(user_id=user_id, isDelete=False).first()
        if user is None:
            return {"message": "user does not exist"}
        user.credit += amount
        try:
            db.session.commit()
            return {"message": f"Credit increased by {amount}", "new_credit": user.credit}
        except Exception as e:
            db.session.rollback()
            return {"message": "Failed to increase credit", "error": str(e)}

    # get user credit
    @staticmethod
    def get_credit(user_id: int):
        user = User.query.filter_by(user_id=user_id, isDelete=False).first()
        if user is None:
            return {"message": "user does not exist"}
        return user.credit

    @staticmethod
    def check_new(user_id: int):
        user = User.query.filter_by(user_id=user_id, isDelete=False).first()
        if user is None:
            return None
        if user.credit >= 10:
            user.is_new = False
        db.session.commit()
        return user
