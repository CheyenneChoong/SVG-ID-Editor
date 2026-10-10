from flask import Blueprint, request, jsonify
from fileManagement.file import fileManagement
from projectManagement.project import Project
from svgEdit.svg import svg

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

@projectBlueprint.route('/uploadFile', methods=['POST'])
def uploadFile():
    upload = request.files['upload-svg']
    data = projectManagement.uploadFile(upload)
    return jsonify({"fileId": data[0], "name": data[1]})

@projectBlueprint.route('/deleteFile', methods=['GET'])
def deleteFile():
    fileId = request.args.get("fileId")
    projectManagement.deleteFile(fileId)
    return jsonify({})

@projectBlueprint.route('/getSvg')
def getSvg():
    data = projectManagement.getFile()
    if data['active'] != "None":
        svg.file(projectId, data['active'])
        svgTag = svg.getSvg()
        fileData = data['files'][data['active']]
        size = svg.getSize()
    else:
        svgTag = ""
        fileData = {}
        size = {}
    return jsonify({"active": data['active'], "svg": svgTag, "data": fileData, "size": size})

@projectBlueprint.route('/selectFile', methods=['GET'])
def selectFile():
    fileId = request.args.get("fileId")
    projectManagement.activeFile(fileId)
    return jsonify({})

@projectBlueprint.route('/zoom', methods=['GET'])
def zoom():
    type = request.args.get("zoom")
    size = svg.getSize()
    data = projectManagement.getFile()
    fileData = data['files'][data['active']]
    zoomValue = fileData["zoom"]
    if type == "zoom-in":
        zoomValue += 2
    else:
        if (zoomValue - 2) >= 1:
            zoomValue -= 2
    projectManagement.updateMode(data['active'], "zoom", zoomValue)
    return jsonify({
        "size": size,
        "zoom": zoomValue
    })

@projectBlueprint.route('/updateMode', methods=['GET'])
def updateMode():
    key = request.args.get("key")
    value = request.args.get("value")
    data = projectManagement.getFile()
    projectManagement.updateMode(data['active'], key, value)
    return jsonify({})