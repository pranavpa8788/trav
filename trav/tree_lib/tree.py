from typing import Optional, List

from trav.data_lib.node import Node
from trav.utils import Utils
from trav.data_lib.depthMap import DepthMap
from trav.terminal_lib.terminal_graphics import TerminalGraphics


class Tree:
    def __init__(
            self,
            headHeight: int,
            tailHeight: int,
            showOnlyDirs: bool,
            showEmptyDirs: bool,
            showDotDirs: bool,
            cycleOnSameLevel: bool) -> None:

        self.maxDepth: int = headHeight + tailHeight

        self.currentNode: Node = None
        self.rootNode: Node = None

        self.showOnlyDirs = showOnlyDirs
        self.showEmptyDirs = showEmptyDirs
        self.showDotDirs = showDotDirs
        self.cycleOnSameLevel = cycleOnSameLevel

        self.depthMap = DepthMap()

    def setCurrentNode(self, node: Node) -> None:
        self.currentNode = node

    def setRootNode(self, node: Node) -> None:
        self.rootNode = node

    def getRootNode(self, head: int) -> Node:
        count = 0
        currentNodePath = self.currentNode.nodePath
        while count != head:
            currentNodePath = currentNodePath.parent
            count += 1
        rootNode = Node(currentNodePath, None, 0, 0)
        return rootNode

    def printVerticalTree(self, node: Node = None, targetNode: Node = None, printNodePaths: bool = False,
                          prefix: str = "",
                          depth: int = -1) -> None:

        node = Utils.normalizeArg(node, self.rootNode, Node.nodePathNoneChecker)
        targetNode = Utils.normalizeArg(targetNode, self.currentNode, Node.nodePathNoneChecker)

        if node == self.rootNode:
            Utils.clearScreen()

        highlightNode = targetNode == node
        Node.printNodeName(node, printNodePaths, prefix, depth, highlightNode)
        for index, child in enumerate(node.childNodes):
            if index != len(node.childNodes) - 1:
                self.printVerticalTree(child, targetNode, printNodePaths,
                                       TerminalGraphics.BOX_DRAWINGS_LIGHT_VERTICAL_AND_RIGHT, depth + 1)
            else:
                self.printVerticalTree(child, targetNode, printNodePaths,
                                       TerminalGraphics.BOX_DRAWINGS_LIGHT_UP_AND_RIGHT, depth + 1)

    def findChildNodeByName(self, nodeName: str, rootNode: Node = None) -> Node:
        rootNode: Node = Utils.normalizeArg(rootNode, self.rootNode, Node.nodePathNoneChecker)

        for childNode in rootNode.childNodes:
            if childNode.nodeName == nodeName:
                return childNode

        for childNode in rootNode.childNodes:
            returnNode = self.findChildNodeByName(nodeName, childNode)
            if returnNode:
                return returnNode

        return None

    def findChildNodesByName(self, nodeName: str, rootNode: Node = None) -> List[Node]:
        rootNode = Utils.normalizeArg(rootNode, self.rootNode, Node.nodePathNoneChecker)

        childNodes = []

        for childNode in rootNode.childNodes:
            if childNode.nodeName == nodeName:
                childNodes.append(childNode)

            childNodes += self.findChildNodesByName(nodeName, childNode)

        return childNodes

    def getMaxDepthChild(self, index: int) -> Node:
        return self.depthMap.data[self.depthMap.maxDepth][index]

    def updateRootNode(self, rootNode: Node = None) -> Optional[Node]:
        rootNode: Node = Utils.normalizeArg(rootNode, self.rootNode, Node.nodePathNoneChecker)

        rootNodePath = rootNode.nodePath
        currentDepth = rootNode.depth

        if self.maxDepthReached(currentDepth):
            return None

        if not Utils.showNonDir(self.showOnlyDirs, rootNodePath):
            return None

        if Utils.isValidDir(rootNodePath, self.showEmptyDirs, self.showDotDirs):
            childCount = 0

            nd = rootNodePath.iterdir()
            while True:
                try:
                    childPath = next(nd)
                    childNode = Node(childPath, rootNode, childCount, currentDepth + 1)
                    childNode = self.updateRootNode(childNode)

                    if childNode is not None:
                        childCount += 1
                        self.depthMap.addNode(currentDepth + 1, childNode)

                        rootNode.addChildNode(childNode)

                        if rootNode == self.currentNode:
                            self.currentNode = rootNode
                except StopIteration:
                    break
                except PermissionError:
                    continue

            return rootNode
        else:
            return rootNode if not Utils.isDir(rootNodePath) else None

    def maxDepthReached(self, depth: int) -> bool:
        return depth == self.maxDepth

    # future enhancement: write tree to file and read file as tree
    def writeTreeToFile(self, filename: str) -> None:
        with open(filename, "w") as file:
            file.write(str(self.rootNode))
        print(f"Tree written to file: {filename}, data: {str(self.rootNode)}")
