from trav.command_parser import CommandParser
from trav.tree_lib.tree import Tree
from trav.tree_lib.tree_builder import TreeBuilder


class TreeDirector:
    def __init__(self, currentNodePath: str):
        self.commandParser = CommandParser(currentNodePath=currentNodePath)
        self.commandParser.parseArgs()
        self.tree: Tree = None

    def constructTree(self) -> Tree:
        TreeBuilder.normalizeCurrentNodePath(self.commandParser)
        self.tree = TreeBuilder.buildTree(self.commandParser)
        return self.tree

    def registerForEvents(self, modeManager):
        TreeBuilder.registerForEvents(self.tree, modeManager)

    def displayTree(self) -> None:
        self.tree.printVerticalTree()

