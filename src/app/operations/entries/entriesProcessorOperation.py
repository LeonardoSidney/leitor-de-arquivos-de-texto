from app.services.entries.insertNewEntryService import insertNewEntryService


class EntriesProcessorOperation:
    def __init__(self):
        pass

    def process(self, token):
        checkTimeInterval = self._findTimeInterval(token[1], token[3], token[4])
        if not checkTimeInterval:
            return True
        insertNewData = insertNewEntryService(token)

        return insertNewData

    def _findTimeInterval(self, location, startTime, endTime):
        return True
