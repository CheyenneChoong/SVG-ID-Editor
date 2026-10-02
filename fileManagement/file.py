import json
import shutil
import os
from datetime import datetime

class FileManagement:
    def __init__(self):
        try: 
            with open('data/file.json', 'r') as file:
                self.data = json.load(file)
        except:
            with open('data/file.json', 'w') as file:
                pass
            self.data = {}

    def getProjects(self):
        return self.data

    def create(self, projectTitle):
        __projectId = datetime.now().strftime('%d%m%Y%H%M%S')
        __dateCreated = datetime.now().strftime('%d-%m-%Y')
        __lastAccessed = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.data[__projectId] = {
            'title': projectTitle,
            'date-created': __dateCreated,
            'last-accessed': __lastAccessed
        }
        with open('data/file.json', 'w') as file:
            json.dump(self.data, file, indent=4)

        os.mkdir(f'projects/{__projectId}')
        with open(f'projects/{__projectId}/project.json', 'w') as file:
            pass

        self.updateAccess(__projectId)

    def update(self, projectId, key, update):
        self.data[projectId][key] = update
        self.updateAccess(projectId)

    def updateAccess(self, projectId):
        __lastAccessed = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.data[projectId]["last-accessed"] = __lastAccessed
        __latest = { projectId: self.data[projectId] }
        del(self.data[projectId])
        __oldData = self.data
        self.data = __latest | __oldData
        with open('data/file.json', 'w') as file:
            json.dump(self.data, file, indent=4)

    def delete(self, projectId):
        del(self.data[projectId])
        with open('data/file.json', 'w') as file:
            json.dump(self.data, file, indent=4)
        shutil.rmtree(f'projects/{projectId}')