from typing import List, Optional


class BinarySearchTreeNode:
    def __init__(self, value) -> None:
        self.value: int = value
        self.left: Optional[BinarySearchTreeNode] = None
        self.right: Optional[BinarySearchTreeNode] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self._root: Optional[BinarySearchTreeNode] = None

    def insert_node(self, new_node: BinarySearchTreeNode) -> None:
        if not self._root:
            self._root = new_node
            return

        nodes: List[BinarySearchTreeNode] = [self._root]

        while nodes:
            current: BinarySearchTreeNode = nodes.pop(0)

            if new_node.value > current.value:
                if current.right:
                    nodes.append(current.right)
                else:
                    current.right = new_node
                    return
            else:
                if current.left:
                    nodes.append(current.left)
                else:
                    current.left = new_node
                    return

    def insert(self, value):
        self.insert_node(BinarySearchTreeNode(value))

    def insert_many(self, values):
        for value in values:
            self.insert(value)


__all__ = [
    "BinarySearchTree",
]
