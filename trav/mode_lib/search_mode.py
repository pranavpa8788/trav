from typing import Optional, List

from trav.data_lib.node import Node
from trav.mode_lib.mode import Mode
from trav.controller_lib.key import KEYS, Key
from trav.terminal_lib.terminal_graphics import TerminalGraphics


class SearchMode(Mode):
    isKeyPressed: bool = False

    searchString: str = ""

    searchPrompt: str = f"{TerminalGraphics.PRINT_AT_BOTTOM}/"

    searchList: List[Node] = []
    searchListIndex = 0

    @staticmethod
    def isAlphaNumericKey(keyValue: Key) -> Optional[str]:
        keyValue = keyValue.primaryValue.split("Key.")[-1]
        if (keyValue.isalnum() or keyValue.startswith(".")) and len(keyValue) == 1:
            return keyValue
        return None

    @classmethod
    def handleKeyPress(cls, keyValue: str):
        key = Key.standardizeKey(keyValue)

        if key == KEYS.ENTER:
            cls.searchList = cls.modeManager.tree.findChildNodesByName(nodeName=cls.searchString)

            cls.searchString = ""

            if cls.searchList:
                cls.modeManager.tree.currentNode = cls.searchList[0]

            cls.modeManager.changeToTraverseMode()

        elif key == KEYS.BACKSPACE:
            cls.searchString = cls.searchString[:-1]

        elif key == KEYS.ESCAPE:
            cls.searchString = ""
            cls.modeManager.changeToTraverseMode()

        elif keyValue := SearchMode.isAlphaNumericKey(key):
            cls.searchString += keyValue

    @classmethod
    def searchNextChild(cls):
        if cls.searchListIndex + 1 < len(cls.searchList):
            cls.searchListIndex += 1
        else:
            cls.searchListIndex = 0
        cls.modeManager.tree.currentNode = cls.searchList[cls.searchListIndex]

    @classmethod
    def searchPreviousChild(cls):
        if cls.searchListIndex - 1 <= 0:
            cls.searchListIndex -= 1
        else:
            cls.searchListIndex = len(cls.searchList) - 1
        cls.modeManager.tree.currentNode = cls.searchList[cls.searchListIndex]

    @classmethod
    def handleKeyRelease(cls, keyValue: str):
        cls.modeManager.tree.printVerticalTree()
        cls.printSearchPrompt()

    @classmethod
    def printSearchPrompt(cls):
        print(f"{cls.searchPrompt}{cls.searchString}", end="", flush=True)
