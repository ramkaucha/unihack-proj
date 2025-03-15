from . import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    likes = db.Column(db.JSON, default=[])
    joins = db.Column(db.JSON, default=[])
    create_date = db.Column(db.DateTime, default=datetime.utc)
    is_archived = db.Column(db.Boolean, default=False)

    # Foreign key to Project
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'), nullable=False)
    project = db.relationship('Project', backref='posts')

    # One-to-many relationship with comments
    comments = db.relationship('Comment', backref='post', lazy=True)
