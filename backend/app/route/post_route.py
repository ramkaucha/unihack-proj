from flask import Blueprint
from ..controller import PostController

post_bp = Blueprint('post', __name__)

# get posts
post_bp.route('/', methods=['GET'])(PostController.get_posts)
# get popular posts
post_bp.route('/popular', methods=['GET'])(PostController.get_posts_sorted_by_popularity)
# get single post
post_bp.route('/<int:post_id>', methods=['GET'])(PostController.get_post)
# create post
post_bp.route('/', methods=['POST'])(PostController.create_post)
# update post
post_bp.route('/<int:post_id>', methods=['PUT'])(PostController.update_post)
# archive post
post_bp.route('/<int:post_id>/archive', methods=['PATCH'])(PostController.archive_post)
# delete post
post_bp.route('/<int:post_id>', methods=['DELETE'])(PostController.delete_post)
# toggle like
post_bp.route('/posts/<int:post_id>/like', methods=['POST'])(PostController.toggle_like)
# toggle join
post_bp.route('/posts/<int:post_id>/join', methods=['POST'])(PostController.toggle_join)