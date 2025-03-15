from flask import jsonify, request
from ..service import CommentService


class CommentController:

    """ get comments
    Args:
        post_id -int -on url path
    Returns:
        comments -see util/schema/comment_schema
    """
    @staticmethod
    def get_comments(post_id):
        try:
            comments, user_dict = CommentService.get_comments_s(post_id)
            return jsonify(comments), 200
        except Exception as e:
            return jsonify({"message": str(e)}), 500

    """ add comment
    Args:
        post_id -int -on url path
        user_id -int -on url path
    Returns: 
        comments -formatted JSON see util/schema/comment_schema
    """
    @staticmethod
    def add_comment(post_id, user_id):
        try:
            data = request.get_json()
            content = data.get("content")
            new_comment = CommentService.add_comment_s(post_id, user_id, content)
            return jsonify(new_comment), 201
        except ValueError as e:
            return jsonify({"message": str(e)}), 400
        except Exception as e:
            return jsonify({"message": "Internal server error"}), 500

    """ update comment
    Args:
        comment_id -int -on url path
    Returns:
        comments -formatted JSON see util/schema/comment_schema
    """
    @staticmethod
    def update_comment(comment_id):
        try:
            data = request.get_json()
            updated_comment = CommentService.update_comment_s(comment_id, data)
            return jsonify(updated_comment), 200
        except ValueError as e:
            return jsonify({"message": str(e)}), 404
        except Exception as e:
            return jsonify({"message": "Internal server error"}), 500

    """ delete comment
    Args:
        comment_id -int -on url path
    Returns:
        comment_id -int
    """
    @staticmethod
    def delete_comment(comment_id):
        try:
            deleted_comment_id = CommentService.delete_comment_s(comment_id)
            return jsonify(deleted_comment_id), 200
        except ValueError as e:
            return jsonify({"message": str(e)}), 404
        except Exception as e:
            return jsonify({"message": "Internal server error"}), 500
