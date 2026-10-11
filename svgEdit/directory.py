from flask import Blueprint, Response, jsonify, request
from svgEdit.svg import svg

svgBlueprint = Blueprint('svg', __name__)

@svgBlueprint.route("/automatic")
def automaticId():
    svg.automatic()
    data = svg.getSvg()
    return jsonify({"svg": data})

@svgBlueprint.route('/manual', methods=['POST'])
def manualId():
    file = request.files['manual-file']
    content = file.read().decode('utf-8')
    svg.manual(content)
    data = svg.getSvg()
    return jsonify({"svg": data})

@svgBlueprint.route("/download", methods=['POST'])
def download():
    data = svg.getSvg()
    return Response(
        data,
        mimetype="image/svg+xml",
        headers={"Content-Disposition": "attachment;filename=output.svg"}
    )

@svgBlueprint.route("/reset")
def reset():
    svg.reset()
    data = svg.getSvg()
    return jsonify({"svg": data})

@svgBlueprint.route("/idList")
def idList():
    return jsonify({"idList": svg.getId()})

@svgBlueprint.route("/saveChange", methods=['GET'])
def saveChange():
    id = request.args.get("id")
    newId = request.args.get("newId")
    fill = request.args.get("fill")
    stroke = request.args.get("stroke")
    svg.updateSvg(id, "fill", fill)
    svg.updateSvg(id, "stroke", stroke)
    svg.updateSvg(id, "id", newId)
    data = svg.getSvg()
    return jsonify({"svg": data})

@svgBlueprint.route("/deleteId", methods=['GET'])
def deleteId():
    id = request.args.get("id")
    svg.deleteId(id)
    data = svg.getSvg()
    return jsonify({"svg": data})

@svgBlueprint.route("/test")
def test():
    data = svg.getTest()
    return jsonify({"svg": data})