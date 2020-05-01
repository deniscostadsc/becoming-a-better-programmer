from typing import List


class EmptyHeap(Exception):
    pass


class MinHeap:
    def __init__(self) -> None:
        self.__heap: List[int] = []

    def __len__(self) -> int:
        return len(self.__heap)

    def __getitem__(self, index: int) -> int:
        return self.__heap[index]

    def __has_parent(self, index: int) -> bool:
        return self.__parent_index(index) >= 0

    def __has_left_child(self, index: int) -> bool:
        return self.__left_child_index(index) < len(self)

    def __has_right_child(self, index: int) -> bool:
        return self.__right_child_index(index) < len(self)

    def __parent(self, index: int) -> int:
        return self.__heap[self.__parent_index(index)]

    def __left_child(self, index: int) -> int:
        return self.__heap[self.__left_child_index(index)]

    def __right_child(self, index: int) -> int:
        return self.__heap[self.__right_child_index(index)]

    def __parent_index(self, index: int) -> int:
        return int((index - 1) / 2)

    def __left_child_index(self, parent_index: int) -> int:
        return parent_index * 2 + 1

    def __right_child_index(self, parent_index: int) -> int:
        return parent_index * 2 + 2

    def __swap(self, first_index: int, second_index: int) -> None:
        self.__heap[first_index], self.__heap[second_index] = (
            self.__heap[second_index],
            self.__heap[first_index],
        )

    def __heapfy_up(self) -> None:
        index = len(self) - 1
        value = self.__heap[index]

        while self.__has_parent(index) and self.__parent(index) > value:
            self.__swap(index, self.__parent_index(index))
            index = self.__parent_index(index)
            value = self.__heap[index]

    def __min_child_index(self, index: int) -> int:
        min_child_index = self.__left_child_index(index)
        if self.__has_right_child(index):
            if self.__right_child(index) < self.__left_child(index):
                min_child_index = self.__right_child_index(index)
        return min_child_index

    def __heapfy_down(self) -> None:
        index = 0
        value = self.__heap[index]

        while self.__has_left_child(index):
            min_child_index = self.__min_child_index(index)

            if value < self.__heap[min_child_index]:
                break
            else:
                self.__swap(index, min_child_index)

            index = min_child_index
            value = self.__heap[index]

    def push(self, value: int) -> None:
        self.__heap.append(value)
        self.__heapfy_up()

    def peek(self) -> int:
        if not len(self):
            raise EmptyHeap("you cannot peek on empty heap")

        return self.__heap[0]

    def pop(self) -> int:
        if not len(self):
            raise EmptyHeap("you cannot pop on empty heap")

        pop = self.__heap[0]
        if len(self) == 1:
            del self.__heap[0]
        else:
            self.__heap[0] = self.__heap[-1]
            del self.__heap[-1]
            self.__heapfy_down()
        return pop


__all__ = ["EmptyHeap", "MinHeap"]
