from flask import Blueprint
from ..controller import (create_post, get_post, get_posts, get_posts_sorted_by_popularity, update_post,
                          archive_post, delete_post, toggle_like, toggle_join)

post_bp = Blueprint('post', __name__)

# get posts
post_bp.route('/', methods=['GET'])(get_posts)
# get popular posts
post_bp.route('/popular', methods=['GET'])(get_posts_sorted_by_popularity)
# get single post
post_bp.route('/<int:post_id>', methods=['GET'])(get_post)
# create post
post_bp.route('/', methods=['POST'])(create_post)
# update post
post_bp.route('/<int:post_id>', methods=['PUT'])(update_post)
# archive post
post_bp.route('/<int:post_id>/archive', methods=['PATCH'])(archive_post)
# delete post
post_bp.route('/<int:post_id>', methods=['DELETE'])(delete_post)
# toggle like
post_bp.route('/posts/<int:post_id>/like', methods=['POST'])(toggle_like)
# toggle join
post_bp.route('/posts/<int:post_id>/join', methods=['POST'])(toggle_join)