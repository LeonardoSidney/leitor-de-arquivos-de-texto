
from app.services.files.loadFileService import loadFileService
from app.services.files.processTextFileService import processTextLineService
from app.services.files.verifyTokensInLineService import verifyTokensInLineService
from domain.enum.enumMenuMessage import EnumMenuMessage
from domain.enum.enumProcessorMessages import EnumProcessorMessages
from infra.logger.logger import Logger

class TextProcessorOperation:
    def __init__(self):
        pass

    def execute(self, file):
        fileContent = loadFileService(file)
        validateFile = self._validateFile(fileContent)
        if not validateFile:
            return False
        return fileContent

    def inputToToken(self, line):
        validateInput = verifyTokensInLineService(line)

        if not validateInput:
            return False

        lineTokenized = processTextLineService(line)
        return lineTokenized

    def _validateFile(self, file):
        lineIsValid = self._verifyTokenInFile(file)
        if not lineIsValid:
            return False
        return True

    def _verifyTokenInFile(self, file):
        for start, line in enumerate(file, start=1):
            isValid = verifyTokensInLineService(line)
            if not isValid:
                Logger().error(EnumProcessorMessages.ERROR_VALIDATE_LINE, f"{start}: {line}")
                break
        return isValid
