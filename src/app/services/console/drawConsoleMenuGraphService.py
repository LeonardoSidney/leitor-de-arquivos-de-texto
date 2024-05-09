
from domain.enum.enumMenuMessage import EnumMenuMessage
import curses

def drawConsoleMenuGraphicalService(language, screen):
    screen.clear()
    height, width = screen.getmaxyx()

    options = EnumMenuMessage.MENU_OPTIONS.value[language]
    chooise = 0

    while True:
        screen.clear()
        for i, option in enumerate(options):
            x = width//2 - len(option)//2
            y = height//2 - len(options)//2 + i
            marker = " > " if i == chooise else "   "
            screen.addstr(y, x, f"{marker}{option}")

        tecla = screen.getch()
        if tecla == curses.KEY_UP and chooise > 0:
            chooise -= 1
        elif tecla == curses.KEY_DOWN and chooise < len(options) - 1:
            chooise += 1
        elif tecla == 10:
            if chooise == len(options) - 1:
                break
