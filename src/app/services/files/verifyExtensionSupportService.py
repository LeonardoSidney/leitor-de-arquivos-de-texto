from domain.enum.enumProcessorMessages import EnumProcessorMessages
from infra.logger.logger import Logger

def verifyExtensionSupportService(files, extension):
    for file in files:
        if not file.lower().endswith(tuple(extension)):
            Logger().error(EnumProcessorMessages.ERROR_EXTENSION_FILE, file.split('.')[-1], file)
            return False
    return True
