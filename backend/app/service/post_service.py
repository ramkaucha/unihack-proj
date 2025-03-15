from ..models import db, Post
from sqlalchemy.sql import func


# get all posts
def get_posts_s():
    posts = Post.query.filter_by(is_archived=False).all()
    return [
        {
            "post_id": post.post_id,
            "title": post.title,
            "description": post.description,
            "create_time": post.create_time,
            "likes": len(post.likes) if post.likes else 0,
            "joins": len(post.joins) if post.joins else 0
        }
        for post in posts
    ]


# get all posts sorted by popularity
def get_posts_sorted_by_popularity_s():
    posts = Post.query.order_by(func.json_array_length(Post.likes).desc()).all()
    return [
        {
            "post_id": post.post_id,
            "title": post.title,
            "description": post.description,
            "create_time": post.create_time,
            "likes": len(post.likes) if post.likes else 0,
            "joins": len(post.joins) if post.joins else 0
        }
        for post in posts
    ]


# get post by id
def get_post_s(post_id):
    post = Post.query.filter_by(is_archived=False).get_or_404(post_id)
    return {
        "post_id": post.post_id,
        "title": post.title,
        "description": post.description,
        "create_time": post.create_time,
        "likes": len(post.likes) if post.likes else 0,
        "joins": len(post.joins) if post.joins else 0
    }


# create post
def create_post_s(data):
    new_post = Post(
        title=data.get('title'),
        description=data.get('description'),
        user_id=data.get('user_id')
    )
    db.session.add(new_post)
    db.session.commit()
    return {"message": "Post created successfully!"}


# update post
def update_post_s(post_id, data):
    post = Post.query.filter_by(is_archived=False).get_or_404(post_id)
    post.title = data.get("title", post.title)
    post.description = data.get("description", post.description)

    db.session.commit()
    return {"message": "Post updated successfully!"}


# archive post
def archive_post_s(post_id):
    post = Post.query.get_or_404(post_id)
    post.is_archived = True
    db.session.commit()
    return {"message": "Post archived successfully!"}


# delete post
def delete_post_s(post_id):
    post = Post.query.filter_by(is_archived=False).get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return {"message": f"Post {post_id} deleted successfully!"}


# toggle list item
def toggle_item_s(post_id, field, user_id):
    post = Post.filter_by(is_archived=False).query.get_or_404(post_id)
    if not hasattr(post, field):
        return {"message": f"Invalid field: {field}"}, 400
    field_list = getattr(post, field)
    if user_id in field_list:
        field_list.remove(user_id)
        message = f"Post {field[:-1]} removed successfully!"
    else:
        field_list.append(user_id)
        message = f"Post {field[:-1]} added successfully!"
    db.session.commit()
    return {"message": message}
