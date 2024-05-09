import shlex

def processTextFileService(file):
    tokens = []
    for line in file:
        token = processTextLineService(line)
        tokens.append(token)
    return tokens

def processTextLineService(line):
    line = line.strip('\n')
    lineInTokens = shlex.split(line)
    return lineInTokens
