
from domain.enum.enumMenuMessage import EnumMenuMessage


def drawConsoleMenuService(language):
    print("Menu:")
    for value, option in enumerate(EnumMenuMessage.MENU_OPTIONS_MESSAGE.value[language], 1):
        print(f"{value}. {option}")
