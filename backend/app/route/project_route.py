from flask import Blueprint
from backend.app.controller.project_controller import ProjectController

project_bp = Blueprint('project', __name__)

# create project
project_bp.route('/<int:post_id>/project/<int:user_id>', methods=['POST'])(ProjectController.create_project)
# get project by id
project_bp.route('/<int:project_id>', methods=['GET'])(ProjectController.get_project)
# update project
project_bp.route('/<int:project_id>/<int:user_id>', methods=['PUT'])(ProjectController.update_project)
# check project status
project_bp.route('/<int:project_id>/<int:user_id>/status', methods=['PATCH'])(ProjectController.check_status)
# add issue
project_bp.route('/<int:project_id>/<int:user_id>/issues', methods=['POST'])(ProjectController.add_issue)
# delete project
project_bp.route('/<int:project_id>/<int:user_id>', methods=['DELETE'])(ProjectController.delete_project)
