from flask import jsonify, request
from ..service import get_comments_s, add_comment_s, update_comment_s, delete_comment_s


# get comments
def get_comments(post_id):
    try:
        comments, user_dict = get_comments_s(post_id)
        return jsonify(comments), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# add comment
def add_comment():
    try:
        data = request.get_json()
        new_comment = add_comment_s(data)
        return jsonify(new_comment), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "Internal server error"}), 500


# update comment
def update_comment(comment_id):
    try:
        data = request.get_json()
        updated_comment = update_comment_s(comment_id, data)
        return jsonify(updated_comment), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except Exception as e:
        return jsonify({"message": "Internal server error"}), 500


# delete comment
def delete_comment(comment_id):
    try:
        deleted_comment_id = delete_comment_s(comment_id)
        return jsonify(deleted_comment_id), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
    except Exception as e:
        return jsonify({"message": "Internal server error"}), 500
