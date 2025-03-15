from flask import jsonify, request
from ..models import db, Post
from sqlalchemy.sql import func


# get all posts
def get_posts():
    posts = Post.query.filter_by(is_archived=False).all()
    posts_data = [
        {
            "post_id": post.post_id,
            "title": post.title,
            "description": post.description,
            "create_date": post.create_date,
            "counter": post.counter,
            "is_archived": post.is_archived
        }
        for post in posts
    ]
    return jsonify(posts_data)


# get all posts sorted by popularity
def get_posts_sorted_by_popularity():
    posts = Post.query.order_by(func.json_array_length(Post.likes).desc()).all()
    return jsonify(posts)


# get post by id
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    post_data = {
        "post_id": post.post_id,
        "title": post.title,
        "description": post.description,
        "create_date": post.create_date,
        "counter": post.counter,
        "is_archived": post.is_archived
    }
    return jsonify(post_data)


# create post
def create_post(request):
    data = request.get_json()
    new_post = Post(
        title=data.get('title'),
        description=data.get('description'),
        user_id=data.get('user_id'),
        post_id=data.get('post_id')  # 如果需要设置 post_id
    )
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully!"}), 201


# update post
def update_post(post_id, request):
    data = request.get_json()
    post = Post.query.get_or_404(post_id)
    post.title = data.get("title", post.title)
    post.description = data.get("description", post.description)
    post.counter = data.get("counter", post.counter)
    post.is_archived = data.get("is_archived", post.is_archived)

    db.session.commit()
    return jsonify({"message": "Post updated successfully!"}), 200


# archive post
def archive_post(post_id):
    post = Post.query.get(post_id)
    if post:
        post.is_archived = True
        db.session.commit()
        return jsonify({"message": "Post archived successfully!"}), 200
    else:
        return jsonify({"message": "Post not found!"}), 404


# delete post
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted successfully!"}), 200
