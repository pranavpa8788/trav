import os

from trav.mode_lib.mode_manager import ModeManager, SearchMode
from trav.data_lib.node import Node
from trav.tree_lib.tree import Tree
from trav.tree_lib.tree_traverser import TreeTraverser
from trav.command_parser import CommandParser
from trav.controller_lib.event_handler import EventHandler
from trav.controller_lib.key import KEYS
from trav.utils import Utils


class TreeBuilder:

    @staticmethod
    def normalizeCurrentNodePath(commandParser: CommandParser):
        currentPath: str = os.getcwd()
        commandParser.currentNodePath = Utils.normalizeArg(commandParser.currentNodePath, currentPath,
                                                           Node.nodePathNoneChecker)

    @staticmethod
    def buildTree(commandParser: CommandParser) -> Tree:
        currentNode = Node(commandParser.currentNodePath, None, -1, -1)

        tree = Tree(commandParser.headHeight, commandParser.tailHeight,
                    commandParser.showOnlyDirs, commandParser.showEmptyDirs,
                    commandParser.showDotDirs, commandParser.cycleOnSameLevel)
        tree.setCurrentNode(currentNode)

        tree.setRootNode(tree.getRootNode(commandParser.headHeight))

        tree.updateRootNode()

        return tree

    @staticmethod
    def registerForEvents(tree: Tree, modeManager: ModeManager):
        treeTraverser = TreeTraverser(tree)

        EventHandler.registerForEvent(KEYS.UP_ARROW, treeTraverser.parentNode)
        EventHandler.registerForEvent(KEYS.K_LOWER, treeTraverser.parentNode)

        EventHandler.registerForEvent(KEYS.J_LOWER, treeTraverser.leftmostChildNode)
        EventHandler.registerForEvent(KEYS.J_UPPER, treeTraverser.rightmostChildNode)
        EventHandler.registerForEvent(KEYS.DOWN_ARROW, treeTraverser.middleChildNode)

        EventHandler.registerForEvent(KEYS.LEFT_ARROW, treeTraverser.leftSiblingNodeInSameLevel)
        EventHandler.registerForEvent(KEYS.H_LOWER, treeTraverser.leftSiblingNodeInSameLevel)
        EventHandler.registerForEvent(KEYS.RIGHT_ARROW, treeTraverser.rightSiblingNodeInSameLevel)
        EventHandler.registerForEvent(KEYS.L_LOWER, treeTraverser.rightSiblingNodeInSameLevel)

        EventHandler.registerForEvent(KEYS.H_UPPER, treeTraverser.leftmostSiblingNodeInSameLevel)
        EventHandler.registerForEvent(KEYS.L_UPPER, treeTraverser.rightmostSiblingNodeInSameLevel)

        EventHandler.registerForEvent(KEYS.G_LOWER, lambda: None)
        EventHandler.registerForEvent(KEYS.GT, treeTraverser.rootNode)
        EventHandler.registerForEvent(KEYS.K_UPPER, treeTraverser.rootNode)

        EventHandler.registerForEvent(KEYS.A_LOWER, treeTraverser.leftmostDeepestChildNode)
        EventHandler.registerForEvent(KEYS.D_LOWER, treeTraverser.rightmostDeepestChildNode)

        EventHandler.registerForEvent(KEYS.Q_LOWER, treeTraverser.leftSiblingNodeInSameDepthLevel)
        EventHandler.registerForEvent(KEYS.E_LOWER, treeTraverser.rightSiblingNodeInSameDepthLevel)

        EventHandler.registerForEvent(KEYS.Q_UPPER, treeTraverser.leftmostSiblingNodeInSameDepthLevel)
        EventHandler.registerForEvent(KEYS.E_UPPER, treeTraverser.rightmostSiblingNodeInSameDepthLevel)

        EventHandler.registerForEvent(KEYS.N_LOWER, SearchMode.searchNextChild)
        EventHandler.registerForEvent(KEYS.N_UPPER, SearchMode.searchPreviousChild)

        EventHandler.registerForEvent(KEYS.ENTER, modeManager.end)
        EventHandler.registerForEvent(KEYS.FORWARD_SLASH, modeManager.changeToSearchMode)

        EventHandler.registerForEvent(KEYS.ESCAPE, modeManager.quit)
