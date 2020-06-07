from typing import List


"""
All numbers in an array with length n+1 are in range from 1 to n, so there is
at least one duplication in the array. How to find any a duplication? Please
don't modify the input array.

https://codercareer.blogspot.com/2016/04/no-59-duplications-in-arrays.html
"""


def duplications_in_arrays(numbers: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    duplications = set()
    repeated = [0 for _, _ in enumerate(numbers)]

    for _, number in enumerate(numbers):
        if repeated[number - 1]:
            duplications.add(number)
        else:
            repeated[number - 1] = 1

    return list(duplications)
