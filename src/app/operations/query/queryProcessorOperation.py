from app.services.query.findProgramByLocationService import findProgramByLocationService


class QueryProcessorOperation:
    def __init__(self, fallbackLocation="BR"):
        self.fallbackLocation = fallbackLocation
        pass

    def process(self, token):
        program = findProgramByLocationService(token[1], token[2])
        if program is None:
            program = findProgramByLocationService(self.fallbackLocation, token[2])
        return program
