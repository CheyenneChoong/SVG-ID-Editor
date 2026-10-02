from flask import Blueprint, request, redirect, url_for, jsonify
from fileManagement.file import FileManagement

fileBlueprint = Blueprint('file', __name__)
fileManagement = FileManagement()

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
    return jsonify({"project": project})

@fileBlueprint.route('/delete', methods=['GET'])
def deleteProject():
    projectId = request.args.get('projectId')
    fileManagement.delete(str(projectId))
    return jsonify({})