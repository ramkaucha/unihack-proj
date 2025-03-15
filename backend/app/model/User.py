from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext import declarative
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    userId = Column('user_id', Integer, primary_key=True, autoincrement=True)
    userName = Column('user_name', type= String(length = 50),  nullable=False)
    password = Column('password', type=String(length = 50), nullable=False)
    email = Column('email', type=String(length = 50), nullable=False)
    credit = Column('credit', Integer, nullable=False, default=0)
    isNew = Column('is_new', Boolean, nullable=False, default=True)
    isDelete = Column('is_delete', Boolean, nullable=False, default=False)