from app.services.files.loadFileService import loadFileService
from app.services.files.processTextFileService import processTextFileService


class TokenProcessorOperation:
    def __init__(self):
        pass

    def processText(self, path):
        file = loadFileService(path)
        fileProcessed = processTextFileService(file)
        return fileProcessed
