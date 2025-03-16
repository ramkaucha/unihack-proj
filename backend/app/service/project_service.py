from datetime import datetime

import backend.app.service.post_service as PostService
from ..model import db, Project
from backend.app.service.user_service import UserService
from ..util import SchemaUtil


class ProjectService:

    # create project
    @staticmethod
    def create_project_s(post_id, user_id, users):
        post = PostService.get_post_s(post_id)
        title = post.title
        description = post.description
        owner_id = post.user_id
        users = users
        project = Project(post, title, description, owner_id, users)
        db.session.add(project)
        db.session.commit()
        return SchemaUtil.format_project(project)

    # get project by id
    @staticmethod
    def get_project_s(project_id):
        return Project.query.get(project_id)

    # update project
    @staticmethod
    def update_project_s(project_id, title, description):
        project = Project.query.get(project_id)
        if not project:
            return None
        project.title = title
        project.description = description
        db.session.commit()
        return project

    # check project status
    @staticmethod
    def check_status_s(project_id, new_status):
        project = Project.query.get(project_id)
        if not project:
            return None
        project.status = new_status
        new_users_count = sum(1 for user in project.users if user.is_new=="True")
        if project.status == "done":
            for user_id in project.users:
                UserService.increase_credit(user_id, 1 + new_users_count)
                UserService.check_new(user_id)
        db.session.commit()
        return project

    # add issue
    @staticmethod
    def add_issue_s(project_id, user_id, content):
        project = Project.query.get(project_id)
        if not project:
            return None
        new_issue = {"user_id": user_id, "content": content, "timestamp": datetime.utcnow().isoformat()}
        project.issues.append(new_issue)
        db.session.commit()
        return True

    # delete project
    @staticmethod
    def delete_project_s(project_id):
        project = Project.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
            return True
        return False
