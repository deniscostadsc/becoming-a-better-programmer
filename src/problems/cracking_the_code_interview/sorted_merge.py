from typing import List, Optional


"""
You are given two sorted arrays, A and B, where A has a large enough buffer at
the end to hold B. Write a method to merge B into A in sorted order.
"""


def sorted_merge(
    iter_a: List[Optional[int]], iter_b: List[int]
) -> List[Optional[int]]:
    """
    Time: O(n)
    Space: O(1)
    """
    index_a = iter_a.index(None) - 1
    index_b = len(iter_b) - 1

    for i in range(len(iter_a) - 1, -1, -1):
        if index_a < 0:
            iter_a[i] = iter_b[index_b]
            index_b -= 1
            continue
        if index_b < 0:
            iter_a[i] = iter_a[index_a]
            index_a -= 1
            continue

        if (
            isinstance(iter_a[index_a], int)
            # line bellow is ignored because of
            # https://github.com/python/mypy/issues/7339
            and iter_a[index_a] > iter_b[index_b]  # type: ignore
        ):
            iter_a[i] = iter_a[index_a]
            index_a -= 1
        else:
            iter_a[i] = iter_b[index_b]
            index_b -= 1

    return iter_a
