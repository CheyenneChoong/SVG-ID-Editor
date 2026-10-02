import json
import os

class Project:
    def __init__(self, projectId):
        self.projectId = projectId
        try:
            with open(f'projects/{self.projectId}/project.json', 'r') as file:
                self.data = json.load(file)
        except:
            os.mkdir(f'projects/{self.projectId}')
            with open(f'projects/{self.projectId}/project.json', 'w') as file:
                pass

    def uploadFile():
        pass

    def deleteFile():
        pass

    def workMode():
        pass
    