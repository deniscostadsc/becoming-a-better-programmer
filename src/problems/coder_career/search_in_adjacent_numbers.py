from typing import List

"""
Given an array where two neighboring elements are adjacent (in absolute
difference 1), can you write an algorithm to search an element in the array and
return its position? If the element appears multiple times, please return the
first occurrence.

For example, if given the array {4, 5, 6, 5, 6, 7, 8, 9, 10, 9} and an element
9, the element appears twice in the array, and the first occurrence is at
position 7.
"""

# TODO: solver in a clever way


def search_in_adjacent_numbers(numbers: List[int], search: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    for index, number in enumerate(numbers):
        if search == number:
            return index

    raise ValueError(f"{search} is not in list")
