def loadFileService(path):
    with open(path) as file:
        lines = file.readlines()
    return lines
