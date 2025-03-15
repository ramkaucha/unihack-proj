from flask import jsonify, request
from ..service import PostService


class PostController:
    # get all posts
    @staticmethod
    def get_posts():
        return jsonify(PostService.get_posts_s()), 200

    # get all posts sorted by popularity
    @staticmethod
    def get_posts_sorted_by_popularity():
        return jsonify(PostService.get_posts_sorted_by_popularity_s()), 200

    # get post by id
    @staticmethod
    def get_post(post_id):
        return jsonify(PostService.get_post_s(post_id)), 200

    # create post
    @staticmethod
    def create_post():
        data = request.get_json()
        if (not data
                or not data.get("title")
                or not data.get("description")
                or not data.get("user_id")):
            return jsonify({"message": "Missing required fields"}), 400
        return jsonify(PostService.create_post_s(data)), 201

    # update post
    @staticmethod
    def update_post(post_id):
        data = request.get_json()
        return jsonify(PostService.update_post_s(post_id, data)), 200

    # archive post
    @staticmethod
    def archive_post(post_id):
        return jsonify(PostService.archive_post_s(post_id)), 200

    # delete post
    @staticmethod
    def delete_post(post_id):
        return jsonify(PostService.delete_post_s(post_id)), 200

    # toggle like
    @staticmethod
    def toggle_like(post_id):
        user_id = request.json.get('user_id')
        if not user_id:
            return jsonify({"message": "user_id is required"}), 400
        return jsonify(PostService.toggle_item_s(post_id, "like", user_id)), 200

    # toggle join
    @staticmethod
    def toggle_join(post_id):
        user_id = request.json.get('user_id')
        if not user_id:
            return jsonify({"message": "user_id is required"}), 400
        return jsonify(PostService.toggle_item_s(post_id, "join", user_id)), 200
