import sys
from pathlib import Path
from typing import Union

from trav.utils import Utils


class CommandParser:
    def __init__(
            self,
            currentNodePath: Union[Path, str] = None,
            showOnlyDirs=False,
            headHeight=3,
            tailHeight=3,
            cycleOnSameLevel=True,
            showDotDirs=False,
            showEmptyDirs=True
    ):
        self.currentNodePath = currentNodePath
        self.showOnlyDirs = showOnlyDirs
        self.headHeight = headHeight
        self.tailHeight = tailHeight
        self.cycleOnSameLevel = cycleOnSameLevel
        self.showDotDirs = showDotDirs
        self.showEmptyDirs = showEmptyDirs

    def __repr__(self) -> str:
        return (f"CommandParser(\n\tcurrentNodePath: {self.currentNodePath}, \n\tshowOnlyDirs: {self.showOnlyDirs}"
                f"\n\theadHeight: {self.headHeight}, \n\ttailHeight: {self.tailHeight}, "
                f"\n\tcycleOnSameLevel: {self.cycleOnSameLevel}, \n\tshowDotDirs: {self.showDotDirs}, "
                f"\n\tshowEmptyDirs: {self.showEmptyDirs})")

    @staticmethod
    def exit() -> None:
        sys.exit(1)

    @staticmethod
    def throwInvalidArgException(arg, argValue):
        print(f"trav: invalid value '{argValue}' for {arg} arg")
        CommandParser.exit()

    @staticmethod
    def parseBooleanArg(arg: str, argValue: str) -> bool:
        if argValue.lower() == "true":
            return True
        elif argValue.lower() == "false":
            return False
        CommandParser.throwInvalidArgException(arg, argValue)

    @staticmethod
    def parseIntegerArg(arg: str, argValue: str) -> int:
        try:
            return int(argValue)
        except ValueError:
            CommandParser.throwInvalidArgException(arg, argValue)

    def parseArgs(self):
        argList = sys.argv[2:]
        count = 0
        while count + 1 < len(argList):
            arg = argList[count]
            argValue = argList[count + 1]
            if (arg == "-p") or (arg == "--path"):
                self.currentNodePath = Utils.standardizePath(Path(argValue))
                count += 2
            elif (arg == "-s") or (arg == "--show-only-dirs"):
                self.showOnlyDirs = CommandParser.parseBooleanArg(arg, argValue)
                count += 2
            elif (arg == "-h") or (arg == "--head"):
                self.headHeight = CommandParser.parseIntegerArg(arg, argValue)
                count += 2
            elif (arg == "-t") or (arg == "--tail"):
                self.tailHeight = CommandParser.parseIntegerArg(arg, argValue)
                count += 2
            elif (arg == "-l") or (arg == "--cycle"):
                self.cycleOnSameLevel = CommandParser.parseBooleanArg(arg, argValue)
                count += 2
            elif (arg == "-a") or (arg == "--all"):
                self.showDotDirs = CommandParser.parseBooleanArg(arg, argValue)
                count += 2
            elif (arg == "-e") or (arg == "--show-empty-dirs"):
                self.showEmptyDirs = CommandParser.parseBooleanArg(arg, argValue)
                count += 2
            else:
                print("trav: Invalid argument provided")
                print("Try trav -h or trav --help for more information")

                CommandParser.exit()

                # Needed for unit testing
                count = len(argList)
