from typing import Iterator, Optional

# TODO:
# add SortedLikedList
# add DoublyLinkedList


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
        Time: O(1)
        Space: O(1)

        This usually takes O(n) for time complexity, but I'm caching the
        linked-list size.
        """
        return self._len

    def __iter__(self) -> Iterator[int]:
        """
        Time: O(n)
        Space: O(1)
        """
        current = self._head

        while current:
            yield current.value
            current = current.next

    def prepend(self, value: int) -> None:
        """
        Time: O(1)
        Space: O(1)
        """
        node = Node()
        node.value = value
        node.next = self._head

        self._head = node
        self._len += 1

    def append(self, value: int) -> None:
        """
        Time: O(1)
        Space: O(1)

        This usually takes O(n) for time complexity, but I'm caching a
        reference to the linked list tail.
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

    def insert(self, index: int, value: int) -> None:
        """
        Time: O(n)
        Space: O(1)
        """
        if index > self._len:
            raise IndexError("linked-list index out of range")

        node = Node()
        node.value = value

        previous = self._head
        current = self._head
        position = 0

        if index == 0:
            node.next = self._head
            self._head = node
            self._len += 1
            return

        while current:
            if position == index:
                node.next = current
                previous.next = node
                self._len += 1
                return

            previous = current
            current = current.next
            position += 1

    def reverse(self) -> None:
        """
        Time: O(n)
        Space: O(1)
        """
        previous = None
        current = self._head
        next_node = None

        self._tail = self._head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self._head = previous

    def remove(self, index: int) -> None:
        """
        Time: O(n)
        Space: O(1)
        """
        if index > self._len:
            raise IndexError("linked-list index out of range")

        previous = None
        current = self._head
        current_index = 0

        while current:
            if index == current_index:
                if not previous:
                    self._head = current.next
                else:
                    previous.next = current.next
                    if not current.next:
                        self._tail = current
                self._len -= 1

            previous = current
            current = current.next
            current_index += 1


__all__ = ["LinkedList"]
