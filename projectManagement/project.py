import json
import os
from datetime import datetime

class Project:
    def __init__(self, projectId):
        self.projectId = projectId
        try:
            with open(f'projects/{self.projectId}/project.json', 'r') as file:
                self.data = json.load(file)
        except:
            __defaultData = {
                "active": "None",
                "files": {}
            }
            if not os.path.isdir(f'projects/{self.projectId}'):
                os.mkdir(f'projects/{self.projectId}')
            with open(f'projects/{self.projectId}/project.json', 'w') as file:
                json.dump(__defaultData, file, indent=4)
            self.data = __defaultData

    def getFile(self):
        return self.data

    def uploadFile(self, file):
        __fileId = datetime.now().strftime('%d%m%Y%H%M%S')
        __originalPath = f'projects/{self.projectId}/original-{__fileId}.svg'
        __workPath = f'projects/{self.projectId}/work-{__fileId}.svg'
        file.save(__originalPath)
        file.save(__workPath)
        __name = file.filename
        __name = __name.replace(".svg", "")

        self.data['active'] = __fileId
        self.data['files'][__fileId] = {
            "name": __name,
            "id-mode": "None",
            "test": "False",
            "zoom-width": 0,
            "zoom-height": 0 
        }
        with open(f'projects/{self.projectId}/project.json', 'w') as file:
            json.dump(self.data, file, indent=4)
        return [__fileId, __name]

    def renameFile(self, fileId, name):
        self.data['files'][fileId]['name'] = name
        with open(f'projects/{self.projectId}/project.json', 'w') as file:
            json.dump(self.data, file, indent=4)
    
    def deleteFile(self, fileId):
        os.remove(f'projects/{self.projectId}/original-{fileId}.svg')
        os.remove(f'projects/{self.projectId}/work-{fileId}.svg')
        del(self.data['file'][fileId])
        self.data['active'] = "None"
        with open(f'projects/{self.projectId}/project.json', 'w') as file:
            json.dump(self.data, file, indent=4)

    def activeFile(self, fileId):
        self.data['active'] = fileId
        with open(f'projects/{self.projectId}/project.json', 'w') as file:
            json.dump(self.data, file, indent=4)

    def updateMode(self, fileId, key, status):
        self.data['files'][fileId][key] = status
        with open(f'projects/{self.projectId}/project.json', 'w') as file:
            json.dump(self.data, file, indent=4)