from typing import List


"""
Define a stack, in which we can get its minimum number with a function min. In
this stack, the time complexity of min(), push() and pop() are all O(1).
"""


class Stack:
    """
    Space: O(n)
    """

    def __init__(self) -> None:
        self.__stack: List[int] = []
        self.__min_stack: List[int] = []

    def push(self, number: int) -> None:
        """
        Time: O(1)
        Space: O(1)
        """
        self.__stack.append(number)
        if not self.__min_stack or number < self.__min_stack[-1]:
            self.__min_stack.append(number)
        else:
            self.__min_stack.append(self.__min_stack[-1])

    def pop(self) -> int:
        """
        Time: O(1)
        Space: O(1)
        """
        if not self.__stack or not self.__min_stack:
            raise IndexError("pop from empty list")

        self.__min_stack.pop()
        return self.__stack.pop()

    def min(self) -> int:
        """
        Time: O(1)
        Space: O(1)
        """

        if not self.__stack or not self.__min_stack:
            raise IndexError("min from empty list")

        return self.__min_stack[-1]
