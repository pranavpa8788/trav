from __future__ import annotations

import sys

from trav.utils import Utils
from trav.tree_lib.tree import Tree
import trav.controller_lib.controller as controller
import trav.mode_lib.mode as mode
from trav.mode_lib.traverse_mode import TraverseMode
from trav.mode_lib.search_mode import SearchMode
from trav.terminal_lib.terminal_graphics import TerminalGraphics


class ModeManager:
    def __init__(self, tree: Tree, controller: controller.Controller, currentMode: mode.Mode = TraverseMode, filename: str = ""):
        self.controller = controller
        self.currentMode = currentMode
        self.tree = tree

        self.filename = filename
        self.listener = None

        self.initModes()
    
    def initfilename(self):
        if Utils.isWindowsOS():
            Utils.normalizeArg(self.filename, r"C:\Windows\Temp\tree_out.txt", Utils.defaultTruthnessChecker)
        if Utils.isLinuxOS():
            Utils.normalizeArg(self.filename, "tmp/tree_out.txt", Utils.defaultTruthnessChecker)

    def initModes(self):
        TraverseMode.modeManager = self
        SearchMode.modeManager = self

    def setMode(self, newMode: type[mode.Mode]):
        self.currentMode = newMode

    def handleKeyPress(self, keyValue: str):
        self.currentMode.handleKeyPress(keyValue)

    def handleKeyRelease(self, keyValue: str):
        self.currentMode.handleKeyRelease(keyValue)

    def changeToSearchMode(self):
        self.setMode(SearchMode)
        SearchMode.printSearchPrompt()

    def changeToTraverseMode(self):
        self.setMode(TraverseMode)
        self.tree.printVerticalTree()

    def end(self):
        self.writeOutToFile()
        TerminalGraphics.clearStdin()
        self.quit()

    def setListener(self, listener):
        self.listener = listener

    def writeOutToFile(self):
        currentNodePath = str(self.tree.currentNode.nodePath)
        with open(self.filename, "w") as treeOutFile:
            treeOutFile.write(currentNodePath)

    def quit(self):
        self.listener.stop()
        sys.exit(0)

