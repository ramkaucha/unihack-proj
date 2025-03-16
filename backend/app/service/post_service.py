# from ..model import db, Post
from model import db, Post
from sqlalchemy.sql import func
from util import SchemaUtil
# from ..util import SchemaUtil
# from service import UserService

from service.user_service import UserService


class PostService:

    # get all posts
    @staticmethod
    def get_posts_s(user_id):
        posts = Post.query.filter_by(is_archived=False).all()
        return [SchemaUtil.format_post(post) for post in posts]

    # get all posts sorted by popularity
    @staticmethod
    def get_posts_sorted_by_popularity_s():
        posts = Post.query.order_by(func.json_array_length(Post.likes).desc()).all()
        return [SchemaUtil.format_post(post) for post in posts]

    # get post by id
    @staticmethod
    def get_post_s(post_id):
        post = Post.query.filter_by(is_archived=False).get_or_404(post_id)
        return SchemaUtil.format_post(post)

    # create post
    @staticmethod
    def create_post_s(user_id, title, description):
        new_post = Post(
            user_id=user_id,
            title=title,
            description=description
        )
        db.session.add(new_post)
        db.session.commit()
        return SchemaUtil.format_post(new_post)

    # update post
    @staticmethod
    def update_post_s(post_id, title, description):
        post = Post.query.filter_by(is_archived=False).get_or_404(post_id)
        post.title = title
        post.description = description
        db.session.commit()
        return SchemaUtil.format_post(post)

    # archive post
    @staticmethod
    def archive_post_s(post_id):
        post = Post.query.get_or_404(post_id)
        post.is_archived = True
        db.session.commit()
        return {"post_id": post_id}

    # delete post
    @staticmethod
    def delete_post_s(post_id):
        post = Post.query.filter_by(is_archived=False).get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return {"post_id": post_id}

    # toggle list item
    @staticmethod
    def toggle_item_s(post_id, field, user_id):
        post = Post.query.filter_by(is_archived=False).get_or_404(post_id)
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

    @staticmethod
    def get_likes_s(post_id):
        post = Post.query.get_or_404(post_id)
        users = UserService.get_users_by_id(post.likes)
        return [SchemaUtil.format_user(user) for user in users]

    @staticmethod
    def get_join_s(post_id):
        post = Post.query.get_or_404(post_id)
        users = UserService.get_users_by_id(post.joins)
        return [SchemaUtil.format_user(user) for user in users]

    @staticmethod
    def get_join_shuffle(post_id):
        post = Post.query.get_or_404(post_id)
        weighted_user = {}
        users = UserService.get_users_by_id(post.joins)
        for index, user in enumerate(users):
            weight_index = 1 / (index + 1)
            weight = user.credit * weight_index
            weighted_user[weight] = user
        sorted_items = sorted(weighted_user.items(), key=lambda item: item[0], reverse=True)
        sorted_users = [user for weight, user in sorted_items]
        return [SchemaUtil.format_user(user) for user in sorted_users]
