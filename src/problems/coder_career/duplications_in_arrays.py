from typing import List


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
