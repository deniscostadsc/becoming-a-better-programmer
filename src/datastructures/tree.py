class Node:
    def __init__(self, value):
        pass


class BinaryTree:
    def __init__(self):
        self._root = None

    def __len__(self):
        if not self._root:
            return 0
        return 1

    def add(self, value):
        self._root = Node(value)
