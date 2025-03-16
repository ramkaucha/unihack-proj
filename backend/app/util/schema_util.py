from ..model import Post, Comment, Project, User


class SchemaUtil:
    @staticmethod
    def format_post(post: Post):
        return {
            "post_id": post.post_id,
            "title": post.title,
            "description": post.description,
            "create_time": post.create_time,
            "likes": len(post.likes) if post.likes else 0,
            "joins": len(post.joins) if post.joins else 0
        }

    @staticmethod
    def format_comments(comment: Comment, user_dict=None):
        return {
            "comment_id": comment.comment_id,
            "content": comment.content,
            "create_time": comment.create_time,
            "user_id": comment.user_id,
            "user_name": user_dict.get(comment.user_id, "Unknown")
        }

    @staticmethod
    def format_project(project: Project):
        return {
            "project_id": project.project_id,
            "title": project.title,
            "description": project.description,
            "owner_id": project.owner_id,
            "status": project.status,
            "issues": project.issues,
            "create_time": project.create_time,
        }

    @staticmethod
    def format_user(user: User):
        return {
            "user_name": user.user_name,
            "email": user.email,
            "credit": user.credit,
            "is_new": user.is_new,
            "profile": user.profile
        }
