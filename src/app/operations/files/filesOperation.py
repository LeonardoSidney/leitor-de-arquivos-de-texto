from app.services.files.verifyFilesInPathService import verifyFilesInPathService
from domain.enum.enumRules import EnumRules
from app.services.files.verifyExtensionSupportService import verifyExtensionSupportService

class FilesOperation:
    def __init__(self, files):
        self.files = files
        pass

    def checkExtensions(self):
        fileIsSupported = verifyExtensionSupportService(self.files, EnumRules.FILES_SUPPORTED.value)
        if not fileIsSupported:
            return False
        return True

    def checkFilesExists(self):
        filesExists = verifyFilesInPathService(self.files)
        if not filesExists:
            return False
        return True
