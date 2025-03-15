from ..models import db, Comment


# get all comments
def get_comments_c(post_id):
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.create_time.desc()).all()
    return [
        {
            "comment_id": comment.comment_id,
            "content": comment.content,
            "create_time": comment.create_time,
            "user_id": comment.user_id
        }
        for comment in comments
    ]


# create comment by id
def add_comment_c(data):
    new_comment = Comment(
        content=data.get("content"),
        post_id=data.get("post_id"),
        user_id=data.get("user_id")
    )
    db.session.add(new_comment)
    db.session.flush()
    db.session.commit()
    return {"message": "Comment added successfully!", "comment_id": new_comment.comment_id}


# update comment
def update_comment_c(comment_id, data):
    comment = Comment.query.get_or_404(comment_id)
    comment.content = data.get("content", comment.content)
    db.session.commit()
    return {"message": "Comment updated successfully!"}


# delete comment
def delete_comment_c(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return {"message": "Comment deleted successfully!"}
