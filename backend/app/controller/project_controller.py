from flask import jsonify, request
from ..service import ProjectService
from ..util import SchemaUtil


class ProjectController:
    """ method: create project
        Args:
            post_id -int -from url path
            user_id -int -from url path
        Expectation:
        {
            `users`: [int] -list of user ids
        }
        Returns:
             users -see util/schema/user_schema
    """
    @staticmethod
    def create_project(post_id, user_id):
        data = request.get_json()
        users = data.get("users")
        project = ProjectService.create_project_s(post_id, user_id, users)
        return jsonify(SchemaUtil.format_project(project)), 201

    """ get project by id
    Args:
        post_id -int -from url path
    Returns:
        project -see util/schema/project_schema
    """
    @staticmethod
    def get_project(project_id):
        project = ProjectService.get_project_s(project_id)
        if not project:
            return jsonify({"message": "Project not found"}), 404
        return jsonify(SchemaUtil.format_project(project)), 200

    """ update project
    Args: 
        project_id -int -from url path
    Expectation:
        {
            "title": "string",
            "description": "string
        }
    Returns: 
        project -see util/schema/project_schema
    """
    @staticmethod
    def update_project(project_id):
        data = request.get_json()
        project = ProjectService.get_project_s(project_id)
        if not project:
            return jsonify({"message": "Project not found"}), 404
        title = data.get("title")
        description = data.get("description")
        updated_project = ProjectService.update_project_s(project_id, title, description)
        return jsonify(SchemaUtil.format_project(updated_project)), 200

    """ check project status
    Args: 
        project_id -int -from url path
    Expectation:
        {
            "status": "string"
        }
    Returns: project -see util/schema/project_schema
    """
    @staticmethod
    def check_status(project_id):
        data = request.get_json()
        new_status = data.get("status")
        project = ProjectService.get_project_s(project_id)
        if not project:
            return jsonify({"message": "Project not found"}), 404
        ProjectService.check_status_s(project_id, new_status)
        return jsonify(new_status), 200

    """ add issue
    Args: 
        project_id -int -from url path
        user_id -int -from url path
    Expectation:
        {
            "content": "string"
        }
    Returns: result true while success
    """
    @staticmethod
    def add_issue(project_id, user_id):
        data = request.get_json()
        user_id = user_id
        content = data.get("content")
        result = ProjectService.add_issue_s(project_id, user_id, content)
        if not result:
            return jsonify({"message": "Project not found"}), 404
        return jsonify({"message": "Issue successfully added"}), 200

    """ delete project
    Args: 
        project_id -int -from url path
    """
    @staticmethod
    def delete_project(project_id):
        project = ProjectService.get_project_s(project_id)
        if not project:
            return jsonify({"message": "Project not found"}), 404
        result = ProjectService.delete_project_s(project_id)
        if not result:
            return jsonify({"message": "Project not found"}), 404
        return jsonify({"message": "Project deleted successfully"}), 200
