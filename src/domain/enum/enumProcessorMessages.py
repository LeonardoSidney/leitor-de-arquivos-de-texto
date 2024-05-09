from enum import Enum

class EnumProcessorMessages(Enum):
    ERROR_EXTENSION_FILE = {
        'pt_BR': "Extensão {} do arquivo {} inválida",
    }
    ERROR_IMPORT_FILES = {
        'en': "Error while importing file {} invalid path",
        'pt_BR': "Erro durante a importação a do arquivo {} caminho inválido"
    }
    ERROR_VALIDATE_LINE = {
        'en': "Error validating line {}.",
        'pt_BR': "Erro ao validar a linha {}"
    }
