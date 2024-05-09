import os;

def checkFileService(param):
    isFile = True
    for file in param:
            if os.path.isfile(file) == False:
                return False
    return isFile
