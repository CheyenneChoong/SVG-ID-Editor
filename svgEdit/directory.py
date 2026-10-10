from flask import Blueprint, Response, jsonify
from svgEdit.svg import svg

svgBlueprint = Blueprint('svg', __name__)

@svgBlueprint.route("/automatic")
def automaticId():
    svg.automatic()
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