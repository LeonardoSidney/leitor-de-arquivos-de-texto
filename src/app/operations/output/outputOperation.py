from app.services.output.outputQueryService import outputQueryService


class OutputOperation:
    def __init__(self):
        self.defaultNoneResult = "noise"
        pass

    def execute(self, query, result):
        queryFormatted = self._formatQuery(query)
        if result is None:
            outputQueryService(queryFormatted, self.defaultNoneResult)
            return
        resultFormatted = self._formatResult(result)
        outputQueryService(queryFormatted, resultFormatted)

    def _formatResult(self, result):
        return f'"{result.location}" "{result.name}"'

    def _formatQuery(self, query):
        return f'"{query[1]}" {query[2]}'
