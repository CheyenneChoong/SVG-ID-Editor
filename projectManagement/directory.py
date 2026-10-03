from flask import Blueprint, request, redirect, url_for, jsonify
from fileManagement.file import fileManagement
from projectManagement.project import Project

projectBlueprint = Blueprint('project', __name__)
projectManagement = ""
projectId = ""

@projectBlueprint.route('/open', methods=['GET'])
def openProject():
    global projectId, projectManagement
    projectId = request.args.get("projectId")
    fileManagement.updateAccess(projectId)
    projectManagement = Project(projectId)
    title = fileManagement.getProjects()[projectId]['title']
    data = projectManagement.getFile()
    return jsonify({
        'title': title,
        'active': data['active'],
        'files': data['files']
    })

@projectBlueprint.route('/upload-file', methods=['POST'])
def uploadFile():
    upload = request.files['upload-svg']
    data = projectManagement.uploadFile(upload)
    return jsonify({"fileId": data[0], "name": data[1]})