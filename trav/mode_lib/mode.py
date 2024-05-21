from abc import ABC, abstractmethod

# from trav.mode_lib.mode_manager import ModeManager


class Mode(ABC):
    modeManager = None

    @classmethod
    @abstractmethod
    def handleKeyPress(cls, keyValue: str):
        pass

    @classmethod
    @abstractmethod
    def handleKeyRelease(cls, keyValue: str):
        pass
