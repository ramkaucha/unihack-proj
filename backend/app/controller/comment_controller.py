from flask import request, jsonify
from ..service import (get_comments_c, add_comment_c, update_comment_c, delete_comment_c)

def get_comments(post_id):
    comments = get_comments_c(post_id)
    return jsonify(comments), 200

def add_comment():
    data = request.get_json()
    if not data or "content" not in data or "post_id" not in data or "user_id" not in data:
        return jsonify({"message": "Missing required fields"}), 400
    response = add_comment_c(data)
    return jsonify(response), 201

def update_comment(comment_id):
    data = request.get_json()
    if not data or "content" not in data:
        return jsonify({"message": "Missing content field"}), 400
    response = update_comment_c(comment_id, data)
    return jsonify(response), 200

def delete_comment(comment_id):
    response = delete_comment_c(comment_id)
    return jsonify(response), 200