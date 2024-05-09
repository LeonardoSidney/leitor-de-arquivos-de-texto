
from app.operations.console.consoleOperation import ConsoleOperation
from app.operations.entries.entriesProcessorOperation import EntriesProcessorOperation
from app.operations.files.fileProcessor.textProcessorOperation import TextProcessorOperation
from app.operations.output.outputOperation import OutputOperation
from app.operations.query.queryProcessorOperation import QueryProcessorOperation
from domain.enum.enumMenuMessage import EnumMenuMessage


class ConsoleController:
    def __init__(self, language="pt_BR"):
        self.language = language
        pass

    def execute(self):
        console  = ConsoleOperation(self.language)
        print("\n" + EnumMenuMessage.PRESENTATION_MESSAGE.value[self.language])
        while True:
            choise = console.execute()

            if choise == "1":
                self._createProgram()
            elif choise == "2":
                self._queryProgram()
            elif choise == "0":
                print(EnumMenuMessage.EXIT_MESSAGE.value[self.language])
                break
            else:
                print(EnumMenuMessage.WRONG_OPTION_MESSAGE.value[self.language])

    def _createProgram(self):
        newProgram = input(EnumMenuMessage.CREATE_MESSAGE.value[self.language])

        lineTokenized = self._processInput(newProgram)
        if not lineTokenized:
            return False

        result = EntriesProcessorOperation().process(lineTokenized)

        if not result:
            print(EnumMenuMessage.CREATE_FAILURE_MESSAGE.value[self.language])

        print(EnumMenuMessage.CREATE_SUCCESS_MESSAGE.value[self.language])
        return result

    def _queryProgram(self):
        queryInput = input(EnumMenuMessage.QUERY_MESSAGE.value[self.language])

        lineTokenized = self._processInput(queryInput)
        if not lineTokenized:
            return False

        queryOperation = QueryProcessorOperation()
        outputOperation = OutputOperation()

        query = queryOperation.process(lineTokenized)
        result = outputOperation.execute(lineTokenized, query)
        return result

    def _processInput(self, input):
        TextProcessor = TextProcessorOperation()
        lineTokenized = TextProcessor.inputToToken(input)
        if not lineTokenized:
            print(EnumMenuMessage.PROCESS_INPUT_ERROR_MESSAGE.value[self.language])

        return lineTokenized


