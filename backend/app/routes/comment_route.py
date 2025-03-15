from flask import Blueprint
from ..controller import (get_comments, add_comment, update_comment, delete_comment)

comment_bp = Blueprint("comment", __name__)

# get comments
comment_bp.route("/<int:post_id>/comments", methods=["GET"])(get_comments)
# add comment
comment_bp.route("/comments", methods=["POST"])(add_comment)
# update comment
comment_bp.route("/comments/<int:comment_id>", methods=["PUT"])(update_comment)
# delete comment
comment_bp.route("/comments/<int:comment_id>", methods=["DELETE"])(delete_comment)