from typing import Iterator


class BaseLinkedList:
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

    def __repr__(self):
        joined_values = " ,".join(str(i) for i in self)

        return f"[{joined_values}]"

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
