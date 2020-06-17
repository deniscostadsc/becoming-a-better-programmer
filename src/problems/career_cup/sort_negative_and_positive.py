from typing import List


"""
Give you an array which has n integers,it has both  positive and negative
integers. Now you need sort this array in a special way. After that, the
negative integers should be in the front, and the positive integers should in
the back.Also the relative position should not be changed.


eg. -1 1 3 -2 2 ans: -1 -2 1 3 2.

o(n)time complexity and o(1) space complexity is perfect.

https://www.careercup.com/question?id=5201559730257920
"""


def first_positive(numbers: List[int], start: int = 0) -> int:
    for index, number in enumerate(numbers[start:], start=start):
        if number >= 0:
            return index
    raise ValueError("No positive number in list")


def sort_negative_and_positive(numbers: List[int]) -> List[int]:
    try:
        first_positive_index = first_positive(numbers)
    except ValueError:
        return numbers

    for index, number in enumerate(numbers):
        if number < 0:
            if index > first_positive_index:
                numbers[first_positive_index], numbers[index] = (
                    numbers[index],
                    numbers[first_positive_index],
                )
                first_positive_index = first_positive(
                    numbers, first_positive_index
                )

    return numbers
