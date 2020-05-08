from typing import Iterator, Optional


class Node:
    def __init__(self) -> None:
        self.value: Optional[int] = None
        self.next = None


class LinkedList:
    def __init__(self):
        self._len = 0
        self._head = None
        self._tail = None

    def __len__(self) -> int:
        """
        O(1)

        This usually takes O(n), but I'm caching the linked-list size.
        """
        return self._len

    def __iter__(self) -> Iterator[int]:
        """
        O(n)
        """
        current = self._head

        while current:
            yield current.value
            current = current.next

    def prepend(self, value: int) -> None:
        """
        O(1)
        """
        node = Node()
        node.value = value
        node.next = self._head

        self._head = node
        self._len += 1

    def append(self, value: int) -> None:
        """
        O(1)

        This usually take O(n), but I'm caching a reference to the linked list
        tail.
        """
        node = Node()
        node.value = value

        if not self._head:
            self._head = node
            self._tail = node
            self._len += 1
            return

        self._tail.next = node
        self._tail = node
        self._len += 1


__all__ = ["LinkedList"]
