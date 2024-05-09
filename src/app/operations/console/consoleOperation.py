
from app.services.console.drawConsoleMenuService import drawConsoleMenuService
from domain.enum.enumMenuMessage import EnumMenuMessage


class ConsoleOperation:
    def __init__(self, language):
        self.language = language

    def execute(self):
        drawConsoleMenuService(self.language)

        choice = input(EnumMenuMessage.INPUT_CHOOSE_OPTION_MESSAGE.value[self.language])
        return choice
