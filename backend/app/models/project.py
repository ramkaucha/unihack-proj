from . import db

class Project(db.Model):
    __tablename__ = 'projects'  # 修正为 __tablename__
    project_id = db.Column(db.Integer, primary_key=True)
    users = db.Column(db.JSON, nullable=False)
    status = db.Column(db.String, default="design")  # [design, develop, done]
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))
    issues = db.Column(db.JSON, default=[]) # user_id, content, and timestamp.