from __future__ import annotations


class CLLNode:
    def __init__(self, nextNode: CLLNode, previousNode: CLLNode):
        self.nextNode = nextNode
        self.previousNode = previousNode


class CLL:
    def __init__(self):
        self.headNode = CLLNode(None, None)

    def addNode(self, node: CLLNode):
        if self.headNode.nextNode == None and self.headNode.previousNode == None:
            self.headNode.nextNode = node
            self.headNode.previousNode = node
            node.nextNode = self.headNode
            node.previousNode = self.headNode