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

    def manual(self, file):
        root = self.svg.getroot()
        __rows = file.split("\n")
        # Colour ref, att, id, final colour
        __idList = [[], [], [], []]
        for __row in __rows:
            __data = __row.split(",")
            __idList[0].append(__data[0].strip())
            __idList[1].append(__data[1].strip())
            __idList[2].append(__data[2].strip())
            __idList[3].append(__data[3].strip())
        for __element in root.iter():
            for __index, __ref in enumerate(__idList[0]):
                if __element.get(__idList[1][__index]) == __ref:
                    __element.set("id", __idList[2][__index])
                    __element.set(__idList[1][__index], __idList[3][__index])
        self.svg.write(f"projects/{self.projectId}/work-{self.fileId}.svg", encoding="utf-8", xml_declaration=True)

    def getId(self):
        root = self.svg.getroot()
        __idList = []
        for element in root.iter():
            if element.get("id") is not None:
                __idList.append([element.get("id"), element.get("fill"), element.get("stroke")])
        return __idList

    def reset(self):
        self.svg = ET.parse(f"projects/{self.projectId}/original-{self.fileId}.svg")
        self.svg.write(f"projects/{self.projectId}/work-{self.fileId}.svg", encoding="utf-8", xml_declaration=True)

    def updateSvg(self, id, attribute, value):
        root = self.svg.getroot()
        for element in root.iter():
            if element.get("id") == id:
                element.set(attribute, value)
        self.svg.write(f"projects/{self.projectId}/work-{self.fileId}.svg", encoding="utf-8", xml_declaration=True)

    def deleteId(self, id):
        root = self.svg.getroot()
        for element in root.iter():
            if element.get("id") == id:
                del element.attrib["id"]
        self.svg.write(f"projects/{self.projectId}/work-{self.fileId}.svg", encoding="utf-8", xml_declaration=True)

    def getTest(self):
        testSvg = ET.parse(f"projects/{self.projectId}/work-{self.fileId}.svg")
        root = testSvg.getroot()
        for element in root.iter():
            if element.get("stroke") is not None and element.get("id") is not None:
                element.set("stroke", "#989898")
                element.set("fill", "none")
                element.set("id", f"test-{element.attrib['id']}")
            elif element.get("id") is not None:
                element.set("fill", "#D9D9D9")
                element.set("id", f"test-{element.attrib['id']}")
                
        return ET.tostring(root, encoding="unicode")

svg = Svg()