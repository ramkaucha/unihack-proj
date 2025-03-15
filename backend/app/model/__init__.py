from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .post import Post
from .user import User
from .comment import Comment
from .project import Project