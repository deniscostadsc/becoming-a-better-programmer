from typing import List


class EmptyHeap(Exception):
    pass


class Heap:
    def __init__(self) -> None:
        self._heap: List[int] = []

    def __len__(self) -> int:
        return len(self._heap)

    def __getitem__(self, index: int) -> int:
        return self._heap[index]

    def _has_parent(self, index: int) -> bool:
        return self._parent_index(index) >= 0

    def _has_left_child(self, index: int) -> bool:
        return self._left_child_index(index) < len(self)

    def _has_right_child(self, index: int) -> bool:
        return self._right_child_index(index) < len(self)

    def _parent(self, index: int) -> int:
        return self._heap[self._parent_index(index)]

    def _left_child(self, index: int) -> int:
        return self._heap[self._left_child_index(index)]

    def _right_child(self, index: int) -> int:
        return self._heap[self._right_child_index(index)]

    def _parent_index(self, index: int) -> int:
        return int((index - 1) / 2)

    def _left_child_index(self, parent_index: int) -> int:
        return parent_index * 2 + 1

    def _right_child_index(self, parent_index: int) -> int:
        return parent_index * 2 + 2

    def _swap(self, first_index: int, second_index: int) -> None:
        self._heap[first_index], self._heap[second_index] = (
            self._heap[second_index],
            self._heap[first_index],
        )

    def push(self, value: int) -> None:
        self._heap.append(value)
        self._heapfy_up()

    def peek(self) -> int:
        if not len(self):
            raise EmptyHeap("you cannot peek on empty heap")

        return self._heap[0]

    def pop(self) -> int:
        if not len(self):
            raise EmptyHeap("you cannot pop on empty heap")

        pop = self._heap[0]
        if len(self) == 1:
            del self._heap[0]
        else:
            self._heap[0] = self._heap[-1]
            del self._heap[-1]
            self._heapfy_down()

        return pop


class MinHeap(Heap):
    def _heapfy_up(self) -> None:
        index = len(self) - 1
        value = self._heap[index]

        while self._has_parent(index) and self._parent(index) > value:
            self._swap(index, self._parent_index(index))
            index = self._parent_index(index)
            value = self._heap[index]

    def _min_child_index(self, index: int) -> int:
        min_child_index = self._left_child_index(index)
        if self._has_right_child(index):
            if self._right_child(index) < self._left_child(index):
                min_child_index = self._right_child_index(index)
        return min_child_index

    def _heapfy_down(self) -> None:
        index = 0
        value = self._heap[index]

        while self._has_left_child(index):
            min_child_index = self._min_child_index(index)

            if value < self._heap[min_child_index]:
                break
            else:
                self._swap(index, min_child_index)

            index = min_child_index
            value = self._heap[index]


class MaxHeap(Heap):
    def _heapfy_up(self) -> None:
        index = len(self) - 1
        value = self._heap[index]

        while self._has_parent(index) and self._parent(index) < value:
            self._swap(index, self._parent_index(index))
            index = self._parent_index(index)
            value = self._heap[index]

    def _max_child_index(self, index: int) -> int:
        max_child_index = self._left_child_index(index)
        if self._has_right_child(index):
            if self._right_child(index) > self._left_child(index):
                max_child_index = self._right_child_index(index)
        return max_child_index

    def _heapfy_down(self) -> None:
        index = 0
        value = self._heap[index]

        while self._has_left_child(index):
            max_child_index = self._max_child_index(index)

            if value > self._heap[max_child_index]:
                break
            else:
                self._swap(index, max_child_index)

            index = max_child_index
            value = self._heap[index]


__all__ = ["EmptyHeap", "MinHeap", "MaxHeap"]
