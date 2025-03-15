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
# get list of users who liked the post
post_bp.route('/post/<int:post_id>/likelist', methods=['GET'])(PostController.get_likes)
# get list of users who wanna join the post
post_bp.route('/post/<int:post_id>/joinlist', methods=['GET'])(PostController.get_joins)
# get list of users who wanna join the post in shuffle order
post_bp.route('/post/<int:post_id>/joinshuffle', methods=['GET'])(PostController.get_join_shuffle)