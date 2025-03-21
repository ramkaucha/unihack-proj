from . import db
from datetime import datetime, timezone


class Post(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    likes = db.Column(db.JSON, default=lambda: [])
    joins = db.Column(db.JSON, default=lambda: [])
    create_time = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_archived = db.Column(db.Boolean, default=False)

    # Foreign key to Project
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'), nullable=False)
    # project = db.relationship('Project', backref='posts')
    project = db.relationship('Project', foreign_keys=[project_id], backref='posts')
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False)

    # One-to-many relationship with comments
    comments = db.relationship('Comment', backref='post', lazy=True)
