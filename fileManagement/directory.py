from flask import Blueprint, request, redirect, url_for
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
    print("Project List")
    return

@fileBlueprint.route('/open')
def openProject():
    print("Open")
    return

@fileBlueprint.route('/delete')
def deleteProject():
    print("Delete")
    return