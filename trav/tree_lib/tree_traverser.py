from trav.tree_lib.tree import Tree


class TreeTraverser:
    def __init__(self, tree: Tree):
        self.tree = tree

    def rootNode(self):
        self.tree.currentNode = self.tree.rootNode

    def leftmostDeepestChildNode(self):
        self.tree.currentNode = self.tree.getMaxDepthChild(0)

    def rightmostDeepestChildNode(self):
        self.tree.currentNode = self.tree.getMaxDepthChild(-1)

    def parentNode(self):
        if (parentNode := self.tree.currentNode.getParentNode()) is not None:
            self.tree.currentNode = parentNode

    def leftmostChildNode(self):
        self.tree.currentNode = self.tree.currentNode.getChildNode(0)

    def rightmostChildNode(self):
        self.tree.currentNode = self.tree.currentNode.getChildNode(-1)

    def middleChildNode(self):
        middle = self.tree.currentNode.childNodesSize // 2
        self.tree.currentNode = self.tree.currentNode.getChildNode(middle)

    def leftSiblingNodeInSameLevel(self):
        if (parentNode := self.tree.currentNode.getParentNode()) is not None:
            levelLength = len(self.tree.currentNode.getParentNode().childNodes) - 1
            if self.tree.cycleOnSameLevel and self.tree.currentNode.levelPosition == 0:
                self.tree.currentNode = parentNode.childNodes[levelLength]
            elif self.tree.currentNode.levelPosition > 0:
                self.tree.currentNode = parentNode.childNodes[self.tree.currentNode.levelPosition - 1]


    def rightSiblingNodeInSameLevel(self):
        if (parentNode := self.tree.currentNode.getParentNode()) is not None:
            levelLength = len(self.tree.currentNode.getParentNode().childNodes) - 1
            if self.tree.cycleOnSameLevel and self.tree.currentNode.levelPosition == levelLength:
                self.tree.currentNode = parentNode.childNodes[0]
            elif self.tree.currentNode.levelPosition < levelLength:
                self.tree.currentNode = parentNode.childNodes[self.tree.currentNode.levelPosition + 1]

    def leftmostSiblingNodeInSameLevel(self):
        if (parentNode := self.tree.currentNode.getParentNode()) is not None:
            self.tree.currentNode = parentNode.childNodes[0]

    def rightmostSiblingNodeInSameLevel(self):
        if (
                (parentNode := self.tree.currentNode.getParentNode()) is not None and
                self.tree.currentNode.levelPosition !=
                (levelLength := len(self.tree.currentNode.getParentNode().childNodes) - 1)):

            self.tree.currentNode = parentNode.childNodes[levelLength]

    def leftSiblingNodeInSameDepthLevel(self):
        if self.tree.currentNode.depthPosition > 0:
            self.tree.currentNode = self.tree.depthMap.data[self.tree.currentNode.depth][
                self.tree.currentNode.depthPosition - 1]

    def rightSiblingNodeInSameDepthLevel(self):
        if self.tree.currentNode.depthPosition < len(self.tree.depthMap.data[self.tree.currentNode.depth]) - 1:
            self.tree.currentNode = self.tree.depthMap.data[self.tree.currentNode.depth][
                self.tree.currentNode.depthPosition + 1]

    def leftmostSiblingNodeInSameDepthLevel(self):
        self.tree.currentNode = self.tree.depthMap.data[self.tree.currentNode.depth][0]

    def rightmostSiblingNodeInSameDepthLevel(self):
        self.tree.currentNode = self.tree.depthMap.data[self.tree.currentNode.depth][-1]
