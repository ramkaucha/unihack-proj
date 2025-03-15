from flask import Blueprint
from ..controller import (
    create_project,
    get_project,
    update_project,
    check_status,
    add_issue,
    delete_project
)

project_bp = Blueprint('project', __name__)

# create project
project_bp.route('/', methods=['POST'])(create_project)
# get project by id
project_bp.route('/<int:project_id>', methods=['GET'])(get_project)
# update project
project_bp.route('/<int:project_id>', methods=['PUT'])(update_project)
# check project status
project_bp.route('/<int:project_id>/status', methods=['PATCH'])(check_status)
# add issue
project_bp.route('/<int:project_id>/issues', methods=['POST'])(add_issue)
# delete project
project_bp.route('/<int:project_id>', methods=['DELETE'])(delete_project)
