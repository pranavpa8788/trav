import os
import platform
from pathlib import Path
from typing import Any, Callable, Optional


class Utils:

    @staticmethod
    def normalizeArg(argValue: Any, defaultValue: Any, noneChecker: Callable[[Any], bool]) -> Any:
        if noneChecker(argValue):
            argValue = defaultValue
        return argValue

    @staticmethod
    def defaultNoneChecker(object_: Any) -> bool:
        return object_ is None

    @staticmethod
    def defaultTruthnessChecker(object_: Any) -> bool:
        return True if object_ else False

    @staticmethod
    def isDir(path: Path) -> bool:
        return path.is_dir()

    @staticmethod
    def isNotDir(path: Path) -> bool:
        return not path.is_dir()

    @staticmethod
    def showNonDir(showOnlyDirs: bool, path: Path):
        if showOnlyDirs and Utils.isNotDir(path):
            return False
        return True

    # TODO: reformat this
    @staticmethod
    def isValidDir(path: Path, showEmptyDirs: bool, showDotDirs: bool) -> bool:
        isDir = Utils.isDir(path)

        if not isDir:
            return False

        # Based on or/and condition, the files which are both dotdirs and emptydirs visibility logic is determined
        return Utils.showDotDir(showDotDirs, path) and Utils.showEmptyDir(showEmptyDirs, path)

    """
    Prevent dot directories being shown when showDotDir is disabled
    Because of the nature of filtering out dot dirs (only case is exclusion)
    """
    @staticmethod
    def showDotDir(showDotDirs: bool, path: Path) -> bool:
        if not showDotDirs and Utils.isDotDir(path):
            return False
        return True

    @staticmethod
    def showEmptyDir(showEmptyDirs: bool, path: Path) -> bool:
        if not showEmptyDirs and Utils.isEmptyDir(path):
            return False
        return True

    @staticmethod
    def isDotDir(path: Path) -> bool:
        return path.name.startswith(".")

    @staticmethod
    def isEmptyDir(path: Path) -> bool:
        try:
            next(path.iterdir())
            return False
        except StopIteration:
            return True

    @staticmethod
    def standardizePath(path: Path) -> Path:
        if path.is_absolute():
            return path
        path = path.resolve(True)
        return path

    @staticmethod
    def clearScreen() -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def isWindowsOS() -> bool:
        return platform.system() == "Windows"

    @staticmethod
    def isLinuxOS() -> bool:
        return platform.system() == "Linux"
