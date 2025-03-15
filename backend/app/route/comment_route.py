from flask import Blueprint
from ..controller import CommentController

comment_bp = Blueprint("comment", __name__)

# get comments
comment_bp.route("/<int:post_id>/comments", methods=["GET"])(CommentController.get_comments)
# add comment
comment_bp.route("/<int:post_id>/comments/<int:user_id>", methods=["POST"])(CommentController.add_comment)
# update comment
comment_bp.route("/comments/<int:user_id>/<int:comment_id>", methods=["PUT"])(CommentController.update_comment)
# delete comment
comment_bp.route("/comments/<int:user_id>/<int:comment_id>", methods=["DELETE"])(CommentController.delete_comment)