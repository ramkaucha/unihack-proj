from ..model import db, Comment
from .user_service import UserService
from ..util import SchemaUtil


class CommentService:

    # get all comments
    @staticmethod
    def get_comments_s(post_id):
        comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.create_time.desc()).all()
        user_ids = {comment.user_id for comment in comments}
        user_dict = UserService.get_user_names_by_ids(user_ids)
        return [SchemaUtil.format_comments(comment, user_dict) for comment in comments]

    # create comment
    @staticmethod
    def add_comment_s(post_id, user_id, content):
        new_comment = Comment(
            post_id=post_id,
            user_id=user_id,
            content=content
        )
        db.session.add(new_comment)
        db.session.commit()
        return new_comment

    # update comment
    @staticmethod
    def update_comment_s(comment_id, data):
        comment = Comment.query.get(comment_id)
        if not comment:
            raise ValueError("Comment not found")
        comment.content = data.get("content", comment.content)
        db.session.commit()
        return comment

    # delete comment
    @staticmethod
    def delete_comment_s(comment_id):
        comment = Comment.query.get_or_404(comment_id)
        db.session.delete(comment)
        db.session.commit()
        return {"message": "Comment deleted successfully", "comment_id": comment.comment_id}
