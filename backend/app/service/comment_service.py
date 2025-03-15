from ..model import db, Comment
from .user_service import get_user_names_by_ids
from ..util import format_comments


# get all comments
def get_comments_s(post_id):
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.create_time.desc()).all()
    user_ids = {comment.user_id for comment in comments}
    user_dict = get_user_names_by_ids(user_ids)
    return [format_comments(comment, user_dict) for comment in comments]


# create comment
def add_comment_s(data):
    if not data.get("content") or not data.get("post_id") or not data.get("user_id"):
        raise ValueError("Missing required fields")

    new_comment = Comment(
        content=data["content"],
        post_id=data["post_id"],
        user_id=data["user_id"]
    )
    db.session.add(new_comment)
    db.session.commit()
    return new_comment


# update comment
def update_comment_s(comment_id, data):
    comment = Comment.query.get(comment_id)
    if not comment:
        raise ValueError("Comment not found")
    comment.content = data.get("content", comment.content)
    db.session.commit()
    return comment


# delete comment
def delete_comment_s(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return {"message": "Comment deleted successfully", "comment_id": comment.comment_id}

