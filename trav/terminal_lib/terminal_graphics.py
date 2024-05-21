import sys

from trav.utils import Utils


class TerminalGraphics:
    BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT = "\u251C\u2500\u2500 "
    BOX_DRAWINGS_HEAVY_VERTICAL_AND_RIGHT = "\u2523\u2501\u2501 "
    BOX_DRAWINGS_LIGHT_UP_AND_RIGHT = "\u2514\u2500\u2500 "
    BOX_DRAWINGS_HEAVY_UP_AND_RIGHT = "\u2517\u2501\u2501 "
    BOX_DRAWINGS_LIGHT_VERTICAL = "\u2502"
    BOX_DRAWINGS_HEAVY_VERTICAL = "\u2503"

    COLOR_FG_BLACK_BG_WHITE = "\033[30;47m"
    COLOR_CLEAR = "\033[0m"

    PRINT_AT_BOTTOM = "\033[999B"

    @staticmethod
    def clearStdin():
        if Utils.isLinuxOS():
            from termios import tcflush, TCIOFLUSH
            tcflush(sys.stdin, TCIOFLUSH)
        elif Utils.isWindowsOS():
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()

    @staticmethod
    def printWithTerminalColor(text: str, prefixText: str, color: str) -> None:
        print(prefixText + color + text + TerminalGraphics.COLOR_CLEAR)
