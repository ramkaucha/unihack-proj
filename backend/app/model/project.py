from . import db
from datetime import datetime, timezone


class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    users = db.Column(db.JSON, nullable=False)
    status = db.Column(db.String, default="design")  # [design, develop, done]
    create_time = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    issues = db.Column(db.JSON, default=lambda: [])  # user_id, content, and timestamp.

    # fk
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
