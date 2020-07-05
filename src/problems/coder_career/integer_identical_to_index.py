from typing import List


"""
Integers in an array are unique and increasingly sorted. Please write a
function/method to find an integer from the array who equals to its index. For
example, in the array {-3, -1, 1, 3, 5}, the number 3 equals its index 3.

https://codercareer.blogspot.com/2014/10/no-57-integer-identical-to-index.html

PS: I'll assume there will be always one, and only one, number equal to its
index.
"""


def identical_to_index(numbers: List[int]) -> int:
    """
    Time: O(log n)
    Space: O(1)
    """
    begin = 0
    end = len(numbers) - 1
    result = 0

    while begin <= end:
        middle = begin + ((end - begin) // 2)
        if numbers[middle] == middle:
            result = middle
            break
        elif numbers[middle] > middle:
            end = middle - 1
        else:
            begin = middle + 1

    return result
