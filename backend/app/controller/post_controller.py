from flask import jsonify, request
from ..service import (
    get_posts_s, get_posts_sorted_by_popularity_s, get_post_s,
    create_post_s, update_post_s, delete_post_s, archive_post_s,
    toggle_item_s
)


def get_posts():
    return jsonify(get_posts_s())


def get_posts_sorted_by_popularity():
    return jsonify(get_posts_sorted_by_popularity_s())


def get_post(post_id):
    return jsonify(get_post_s(post_id))


def create_post():
    data = request.get_json()
    return jsonify(create_post_s(data)), 200


def update_post(post_id):
    data = request.get_json()
    return jsonify(update_post_s(post_id, data)), 200


def archive_post(post_id):
    return jsonify(archive_post_s(post_id)), 200


def delete_post(post_id):
    return jsonify(delete_post_s(post_id)), 200


def toggle_like(post_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"message": "user_id is required"}), 400
    return jsonify(toggle_item_s(post_id, "like", user_id)), 200


def toggle_join(post_id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"message": "user_id is required"}), 400
    return jsonify(toggle_item_s(post_id, "join", user_id)), 200
