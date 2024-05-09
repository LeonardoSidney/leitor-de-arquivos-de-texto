import os
from domain.enum.enumProcessorMessages import EnumProcessorMessages

from infra.logger.logger import Logger

def verifyFilesInPathService(files):
    for file in files:
        if not os.path.exists(file):
            Logger().error(EnumProcessorMessages.ERROR_IMPORT_FILES, file)
            return False
    return True
