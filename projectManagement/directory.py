from flask import Blueprint, request, redirect, url_for, jsonify
from fileManagement.file import FileManagement
from projectManagement.project import Project

fileBlueprint = Blueprint('file', __name__)
fileManagement = FileManagement()
projectManagement = ""
projectId = ""

@fileBlueprint.route('/new', methods=['GET'])
def openProject():
    global projectId, projectManagement
    projectId = request.args.get("projectId")
    projectManagement = Project(projectId)
    title = fileManagement.getProjects()[projectId]['title']
    return jsonify({
        'title': title
    })