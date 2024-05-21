from typing import List, Dict

from trav.data_lib.node import Node


class DepthMap:
    def __init__(self):
        self.data: Dict[int, List[Node]] = {}
        self.maxDepth = 0

    def addNode(self, depth: int, node: Node) -> None:
        if node is not None:
            try:
                self.data[depth].append(node)
            except KeyError:
                self.data[depth] = []
                self.data[depth].append(node)

            node.depthPosition = len(self.data[depth]) - 1

            self.maxDepth = depth if depth > self.maxDepth else self.maxDepth

    def __repr__(self) -> str:
        outputStr = "DepthMap("

        for depth, nodes in self.data.items():
            outputStr += f"\n\n\tdepth: {depth},"

            for node in nodes:
                outputStr += f"\n\tnode: {node.nodeName},"

        outputStr += "\n)"
        return outputStr
