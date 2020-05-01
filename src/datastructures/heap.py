from typing import List


class EmptyHeap(Exception):
    pass


class MinHeap:
    def __init__(self) -> None:
        self.__heap: List[int] = []

    def __len__(self) -> int:
        return len(self.__heap)

    def __has_parent(self, index: int) -> bool:
        return self.__parent_index(index) >= 0

    def __parent(self, index: int) -> int:
        return self.__heap[self.__parent_index(index)]

    def __parent_index(self, index: int) -> int:
        return int(index - 1 / 2)

    def __swap(self, first_index: int, second_index: int) -> None:
        self.__heap[first_index], self.__heap[second_index] = (
            self.__heap[second_index],
            self.__heap[first_index],
        )

    def __heapfy_up(self) -> None:
        value = self.__heap[-1]
        index = len(self) - 1

        while self.__has_parent(index):
            if self.__parent(index) <= value:
                break

            self.__swap(index, self.__parent_index(index))
            index = self.__parent_index(index)

    def push(self, value: int) -> None:
        self.__heap.append(value)
        self.__heapfy_up()

    def peek(self) -> int:
        if not len(self):
            raise EmptyHeap("you cannot peek on empty heap")

        return self.__heap[0]

    def pop(self) -> int:
        pop = self.__heap[0]
        del self.__heap[0]
        return pop


__all__ = ["EmptyHeap", "MinHeap"]
