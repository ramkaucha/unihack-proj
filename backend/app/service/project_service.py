from datetime import datetime
from ..model import db, Project
from ..service import UserService


class ProjectService:

    # create project
    @staticmethod
    def create_project_s(title, description, owner_id, users, post_id):
        project = Project(
            title=title,
            description=description,
            owner_id=owner_id,
            users=users,
            post_id=post_id
        )
        db.session.add(project)
        db.session.commit()
        return project

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
        return project

    # delete project
    @staticmethod
    def delete_project_s(project_id):
        project = Project.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
            return True
        return False
