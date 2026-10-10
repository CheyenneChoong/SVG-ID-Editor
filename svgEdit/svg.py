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

    def getSize(self):
        root = self.svg.getroot()
        return {
            "width": root.get("width"),
            "height": root.get("height")
        }

    def automatic(self):
        root = self.svg.getroot()
        count = 0
        for element in root.iter():
            if count != 0:
                element.set("id", f"ID{count}")
            count += 1
        self.svg.write(f"projects/{self.projectId}/work-{self.fileId}.svg", encoding="utf-8", xml_declaration=True)

    def reset(self):
        self.svg = ET.parse(f"projects/{self.projectId}/original-{self.fileId}.svg")
        self.svg.write(f"projects/{self.projectId}/work-{self.fileId}.svg", encoding="utf-8", xml_declaration=True)

    # def manual(self, file):
    #     root = self.svg.getroot()
    #     __rows = file.split("\n")
    #     __idList = [[], [], []]
    #     self.svg.write(f"projects/{self.projectId}/work-{self.fileId}.svg", encoding="utf-8", xml_declaration=True)

svg = Svg()