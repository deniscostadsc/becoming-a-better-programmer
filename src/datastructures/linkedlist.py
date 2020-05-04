class Node:
    def __init__(self) -> None:
        self.value = None
        self.next = None


class LinkedList:
    def __init__(self):
        self._len = 0
        self._head = None

    def __len__(self) -> int:
        return self._len

    def append(self, value: int) -> None:
        if not self._head:
            self._head = Node()
            self._head.value = value
            self._len += 1
            return

        current = self._head
        while current.next:
            current = current.next
        current.next = Node()
        current.next.value = value
        self._len += 1


__all__ = ["LinkedList"]
