from flask import jsonify, request
from ..service import (
    create_project_s,
    get_project_s,
    update_project_s,
    check_status_s,
    add_issue_s,
    delete_project_s
)
from ..util import format_project


# create project
def create_project():
    data = request.get_json()
    if (not data
            or not data.get("title")
            or not data.get("description")
            or not data.get("owner_id")
            or not data.get("users")
            or not data.get("post_id")):
        return jsonify({"message": "Missing required fields"}), 400
    project = create_project_s(
        data["title"],
        data["description"],
        data["owner_id"],
        data["users"],
        data["post_id"]
    )
    return jsonify(format_project(project)), 201


# get project by id
def get_project(project_id):
    project = get_project_s(project_id)
    if not project:
        return jsonify({"message": "Project not found"}), 404
    return jsonify(format_project(project)), 200


# update project
def update_project(project_id):
    data = request.get_json()
    project = get_project_s(project_id)
    if not project:
        return jsonify({"message": "Project not found"}), 404
    updated_project = update_project_s(project_id, data.get("title"), data.get("description"))
    return jsonify(format_project(updated_project)), 200


# check project status
def check_status(project_id):
    data = request.get_json()
    new_status = data.get("status")
    project = get_project_s(project_id)
    if not project:
        return jsonify({"message": "Project not found"}), 404
    updated_project = check_status_s(project_id, new_status)
    return jsonify(new_status), 200


# add issue
def add_issue(project_id):
    data = request.get_json()
    user_id = data.get("user_id")
    content = data.get("content")
    project = add_issue_s(project_id, user_id, content)
    if not project:
        return jsonify({"message": "Project not found"}), 404
    return jsonify({"message": "Issue successfully added"}), 200


# delete project
def delete_project(project_id):
    project = get_project_s(project_id)
    if not project:
        return jsonify({"message": "Project not found"}), 404
    result = delete_project_s(project_id)
    if not result:
        return jsonify({"message": "Project not found"}), 404
    return jsonify({"message": "Project deleted successfully"}), 200


