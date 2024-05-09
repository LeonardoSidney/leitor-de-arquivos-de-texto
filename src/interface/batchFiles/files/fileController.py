import sys
from app.operations.files.fileProcessor.textProcessorOperation import TextProcessorOperation
from app.operations.entries.entriesProcessorOperation import EntriesProcessorOperation
from app.operations.files.fileProcessor.tokenProcessorOperation import TokenProcessorOperation
from app.operations.output.outputOperation import OutputOperation
from app.operations.query.queryProcessorOperation import QueryProcessorOperation
from app.operations.files.filesOperation import FilesOperation

class FileController:
    def __init__(self):
        self.files = sys.argv[1:]
        pass

    def execute(self):
        File = FilesOperation(self.files)
        verifyExtensions = File.checkExtensions()
        if not verifyExtensions:
            return
        verifyFilesExists = File.checkFilesExists()
        if not verifyFilesExists:
            return
        verifyFilesContent = self._verifyFilesContent()
        if not verifyFilesContent:
            return
        tokenizeFiles = self._tokenizeFiles()
        self._processInstructions(tokenizeFiles)

    def _verifyFilesContent(self):
        TextProcessor = TextProcessorOperation()
        for file in self.files:
            extensionFile = file.split('.')[-1]
            if extensionFile == 'txt':
                fileIsValid = TextProcessor.execute(file)
                if not fileIsValid:
                    return False
        return True

    def _tokenizeFiles(self):
        tokens = []
        for file in self.files:
            extensionFile = file.split('.')[-1]
            if extensionFile == 'txt':
                processFile = TokenProcessorOperation().processText(file)
            tokens += processFile
        return tokens

    def _processInstructions(self, tokens):
        entryOperation = EntriesProcessorOperation()
        queryOperation = QueryProcessorOperation()
        outputOperation = OutputOperation()
        for token in tokens:
            if token[0] == 'S':
                entryOperation.process(token)
            if token[0] == 'Q':
                query = queryOperation.process(token)
                outputOperation.execute(token, query)
