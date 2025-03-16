from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean


# db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    credit = db.Column(db.Integer, nullable=False, default=0)
    isNew = db.Column(db.Boolean, nullable=False, default=True)
    isDelete = db.Column(db.Boolean, nullable=False, default=False)
