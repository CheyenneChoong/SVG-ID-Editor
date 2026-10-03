from flask import Blueprint, request, redirect, url_for, jsonify
from fileManagement.file import fileManagement

fileBlueprint = Blueprint('file', __name__)

@fileBlueprint.route('/new', methods=['POST'])
def newProject():
    title = request.form.get("title")
    title = title.replace('"', "")
    title = title.replace("'", "")
    if title:
        fileManagement.create(title)
    return redirect(url_for('home'))

@fileBlueprint.route('/projectList')
def projectList():
    project = fileManagement.getProjects()
    projectIds = project.keys()
    data = []
    for projectId in projectIds:
        data.append([projectId, project[projectId]])
    return jsonify({"project": data})

@fileBlueprint.route('/delete', methods=['GET'])
def deleteProject():
    projectId = request.args.get('projectId')
    fileManagement.delete(str(projectId))
    return jsonify({})