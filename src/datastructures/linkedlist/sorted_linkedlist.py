from .base import BaseLinkedList
from .node import Node


class SortedLinkedList(BaseLinkedList):
    def insert(self, value: int) -> None:
        """
        Time: O(n)
        Space: O(1)
        """
        node = Node()
        node.value = value

        if not self._head:
            self._head = node
            self._tail = node
            self._len += 1
            return

        if node.value < self._head.value:
            node.next = self._head
            self._head = node
            self._len += 1
            return

        current = self._head

        while current.next:
            if node.value < current.next.value:
                node.next = current.next
                current.next = node
                self._len += 1
                return

            current = current.next

        current.next = node
        self._len += 1
