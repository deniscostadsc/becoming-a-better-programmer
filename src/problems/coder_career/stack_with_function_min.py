from typing import List


"""
Define a stack, in which we can get its minimum number with a function min. In
this stack, the time complexity of min(), push() and pop() are all O(1).
"""


class Stack:
    def __init__(self) -> None:
        self.__stack: List[int] = []

    def push(self, number: int) -> None:
        """
        Time: O(1)
        Space: O(1)
        """
        self.__stack.append(number)

    def pop(self) -> int:
        """
        Time: O(1)
        Space: O(1)
        """
        return self.__stack.pop()

    def min(self) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        return min(self.__stack)
