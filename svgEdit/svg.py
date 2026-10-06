import xml.etree.ElementTree as ET

ET.register_namespace("", "http://www.w3.org/2000/svg")

class Svg:
    def __init__(self):
        self.projectId = ""
        self.fileId = ""
        self.svg = ""

    def file(self, projectId, fileId):
        self.projectId = projectId
        self.fileId = fileId
        self.svg = ET.parse(f"projects/{self.projectId}/work-{self.fileId}.svg")

    def getSvg(self):
        root = self.svg.getroot()
        return ET.tostring(root, encoding="unicode")

svg = Svg()