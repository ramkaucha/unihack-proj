from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean


db = SQLAlchemy()

class user(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(String(50), nullable=False, unique=True)
    password = db.Column(String(50), nullable=False)
    email = db.Column(String(50), nullable=False, unique=True)
    credit = db.Column(Integer, nullable=False, default=0)
    isNew = db.Column(Boolean, nullable=False, default=True)
    isDelete = db.Column(Boolean, nullable=False, default=False)
