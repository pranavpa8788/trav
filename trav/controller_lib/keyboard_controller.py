from trav.mode_lib.mode_manager import ModeManager
from trav.controller_lib.controller import Controller
from trav.controller_lib.key import keyToString


class KeyboardController(Controller):
    def __init__(self) -> None:
        self.modeManager = None

    @keyToString
    def handleKeyPress(self, keyValue: str):
        self.modeManager.handleKeyPress(keyValue)

    @keyToString
    def handleKeyRelease(self, keyValue: str):
        self.modeManager.handleKeyRelease(keyValue)

