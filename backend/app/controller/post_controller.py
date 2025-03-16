from flask import jsonify, request
from backend.app.service.post_service import PostService


class PostController:
    """ get all posts
    Returns:
         posts -see util/schema/post_schema
    """
    @staticmethod
    def get_posts():
        return jsonify(PostService.get_posts_s()), 200

    """ get all posts sorted by popularity
    Returns:
        posts -see util/schema/post_schema
    """
    @staticmethod
    def get_posts_sorted_by_popularity():
        return jsonify(PostService.get_posts_sorted_by_popularity_s()), 200

    """ get post by id
    Returns:
        post -see util/schema/post_schema
    """
    # get post by id
    @staticmethod
    def get_post(post_id):
        return jsonify(PostService.get_post_s(post_id)), 200

    """ create post
    Args: 
        user_id -int -from url path
    Expectation:
        {
            "title": "string",
            "description": "string"
        }
    Returns: post -see util/schema/post_schema
    """
    @staticmethod
    def create_post(user_id):
        data = request.get_json()
        if (not data
                or not data.get("title")
                or not data.get("description")):
            return jsonify({"message": "Missing required fields"}), 400
        title = data.get("title")
        description = data.get("description")
        return jsonify(PostService.create_post_s(user_id, title, description)), 201

    """ update post
    Args:
        post_id -int -from url path
    Expectation: 
        {
            "title": "string",
            "description": "string"
        }
    Returns: 
        post -see util/schema/post_schema
    """
    @staticmethod
    def update_post(post_id):
        data = request.get_json()
        if (not data
                or not data.get("title")
                or not data.get("description")):
            return jsonify({"message": "Missing required fields"}), 400
        title = data.get("title")
        description = data.get("description")
        return jsonify(PostService.update_post_s(post_id, title, description)), 200

    """ archive post
    Args: 
        post_id -int -from url path
    Returns: 
        post_id -int
    """
    @staticmethod
    def archive_post(post_id):
        return jsonify(PostService.archive_post_s(post_id)), 200

    """ delete post
    Args:
        post_id -int -from url path
    Returns:
        post_id -int
    """
    @staticmethod
    def delete_post(post_id):
        return jsonify(PostService.delete_post_s(post_id)), 200

    """ when it the button, like the post if not liked, unlike if liked
    Args:
        post_id -int -from url path
        user_id -int -from request body
    """
    @staticmethod
    def toggle_like(post_id, user_id):
        return jsonify(PostService.toggle_item_s(post_id, "like", user_id)), 200

    """ when it the button, join the post if not joined, join if joined
    Args:
        post_id -int -from url path
        user_id -int -from request body
    """
    @staticmethod
    def toggle_join(post_id, user_id):
        return jsonify(PostService.toggle_item_s(post_id, "join", user_id)), 200

    """ get list of users who likes the post
    Args:
        post_id -int -from url path
        users -see util/schema/user_schema
    """
    # get list of users who likes
    @staticmethod
    def get_likes(post_id):
        likes = PostService.get_likes_s(post_id)
        return jsonify(likes), 200

    """ get list of users who wanna join the post
    Args:
        post_id -int -from url path
        users -see util/schema/user_schema
    """
    @staticmethod
    def get_joins(post_id):
        joins = PostService.get_join_s(post_id)
        return jsonify(joins), 200

    """ get list of users who wanna join in shuffle order
    Args:
        post_id -int -from url path
        users -see util/schema/user_schema
    """
    @staticmethod
    def get_join_shuffle(post_id):
        join_shuffle = PostService.get_join_shuffle(post_id)
        return jsonify(join_shuffle), 200
