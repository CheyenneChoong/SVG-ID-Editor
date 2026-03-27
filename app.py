from flask import Flask, render_template, request, redirect, url_for, Response
import xml.etree.ElementTree as ET

ET.register_namespace("", "http://www.w3.org/2000/svg")

class Editor():
    def __init__(self):
        self.imageCode = ""
        self.imageExport = ""
        self.idList = []
    
    def setImage(self, image):
        self.imageCode = image
        self.imageExport = image
    
    def getImage(self):
        return self.imageCode

    def setIDList(self, file):
        rows = file.split("\n")
        self.idList = [[], [], []]
        for row in rows:
            data = row.split(",")
            self.idList[0].append(data[0].strip())
            self.idList[1].append(data[1].strip())
            self.idList[2].append(data[2].strip())
    
    def format(self, root):
        for element in root.iter():
            if element.tag.startswith("{"):
                element.tag = element.tag.split("}", 1)[1]
        return root

    def idSVG(self):
        if not self.idList:
            return
        root = ET.fromstring(self.imageCode)
        for element in root.iter():
            if "fill" in element.attrib:
                if element.attrib["fill"] in self.idList[0]:
                    index = self.idList[0].index(element.attrib["fill"])
                    element.set("id", self.idList[1][index])
                    element.set("fill", self.idList[2][index])
        root = self.format(root)
        self.imageCode = ET.tostring(root, encoding="unicode")
        self.imageExport = ET.tostring(root, encoding="unicode")
    
    def highlight(self, id, color):
        self.imageCode = self.imageExport
        root = ET.fromstring(self.imageCode)
        for element in root.iter():
            if "id" in element.attrib:
                if element.attrib["id"] == id:
                    element.set("fill", color)
        root = self.format(root)
        self.imageCode = ET.tostring(root, encoding="unicode")
    
    def export(self):
        if not self.imageExport:
            return
        root = ET.fromstring(self.imageExport)
        if "xmlns" not in root.attrib:
            root.set("xmlns", "http://www.w3.org/2000/svg")
        root = self.format(root)
        self.imageExport = ET.tostring(root, encoding="unicode")
        return self.imageExport

editor = Editor()

app = Flask(__name__)
@app.route('/')
def home():
    if editor.getImage() is not None:
        code = f"<div id='svg-preview'>{editor.getImage()}</div>"
    else:
        code = "<div id-'svg-preview></div>"
    return render_template('index.html', preview = code)

@app.route('/uploadSVG', methods = ['POST'])
def uploadSVG():
    file = request.files['svgFile']
    content = file.read().decode('utf-8')   # decode bytes into text
    editor.setImage(content)
    return redirect(url_for('home'))

@app.route('/uploadText', methods = ['POST'])
def uploadText():
    file = request.files['idFile']
    content = file.read().decode('utf-8')
    editor.setIDList(content)
    return redirect(url_for('home'))

@app.route('/idSVG', methods = ['POST'])
def idSVG():
    editor.idSVG()
    return redirect(url_for('home'))

@app.route('/highlight', methods = ['POST'])
def highlight():
    idInput = request.form['idInput']
    colorInput = request.form['color']
    editor.highlight(idInput, colorInput)
    return redirect(url_for('home'))

@app.route('/export', methods = ['POST'])
def export():
    svg = editor.export()
    return Response(
        svg,
        mimetype="image/svg+xml",
        headers={"Content-Disposition": "attachment;filename=output.svg"}
    )

if __name__ == '__main__':
    app.run(debug=True)