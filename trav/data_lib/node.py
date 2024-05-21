from __future__ import annotations

from pathlib import Path
from typing import List, Optional, Union

from trav.utils import Utils
from trav.terminal_lib.terminal_graphics import TerminalGraphics


class Node:
    def __init__(self, nodePath: Union[Path, str], parentNode: Optional[Node], levelPosition: int, depth: int) -> None:
        self.nodePath: Path = Utils.standardizePath(Path(nodePath) if type(nodePath) == str else nodePath)
        self.nodeName: str = self.nodePath.name

        self.childNodes: List[Node] = []
        self.childNodesSize = 0

        self.parentNode: Node = parentNode
        self.levelPosition: int = levelPosition
        self.depth: int = depth
        self.depthPosition: int = -1

    def __repr__(self) -> str:
        return (f"\nNode("
                f"\n\tname = {self.nodeName},"
                f"\n\tpath = {self.nodePath},"
                f"\n\tparentNode: {self.parentNode.nodeName if self.parentNode is not None else None},"
                f"\n\tlevelPosition = {self.levelPosition},"
                f"\n\tdepth = {self.depth},"
                f"\n\tchildNodes = {self.childNodes}")

    def __eq__(self, other: Node):
        return self.nodeName == other.nodeName and self.nodePath == other.nodePath #and self.childNodes == other.childNodes

    def addChildNode(self, childNode: Node):
        if childNode is not None:
            self.childNodes.append(childNode)
            self.childNodesSize += 1

    def getParentNode(self) -> Node:
        return self.parentNode

    # May need to be deprecated
    def getChildNode(self, index: int):
        return self.childNodes[index] if len(self.childNodes) > 0 else self

    def printChildNodes(self) -> None:
        for child in self.childNodes:
            print(child)

    @staticmethod
    def printNodeName(node: Node, printNodePath: bool, prefix: str, indentCount: int, highlightNode: bool) -> None:
        nodeStr = node.nodeName if not printNodePath else str(node.nodePath)
        indentCount = 0 if indentCount <= 0 else indentCount
        verticalBarPrefix = TerminalGraphics.BOX_DRAWINGS_LIGHT_VERTICAL * int(indentCount > 0)
        prefixStr = verticalBarPrefix + "\t" * indentCount + prefix
        print(f"{prefixStr}{nodeStr}") if not highlightNode else TerminalGraphics.printWithTerminalColor(
                                                    nodeStr, prefixStr, TerminalGraphics.COLOR_FG_BLACK_BG_WHITE)

    @staticmethod
    def nodePathNoneChecker(nodePath: Union[Path, str]):
        if (nodePath is None) or (not nodePath):
            return True
        return False