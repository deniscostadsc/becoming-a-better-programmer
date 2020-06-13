from itertools import chain
from typing import List


"""
You have k lists of sorted integers. Find the smallest range that includes at
least one number from each of the k lists.

For example,

List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]

The smallest range here would be [20, 24] as it contains 24 from list 1, 20
from list 2, and 22 from list 3.

https://www.careercup.com/question?id=16759664
"""


def included_in_range(iterable, lower_bound, upper_bound):
    begin = 0
    end = len(iterable) - 1

    while begin <= end:
        middle = begin + ((end - begin) // 2)

        if iterable[middle] > lower_bound and iterable[middle] < upper_bound:
            return True

        elif iterable[middle] < lower_bound:
            begin = middle + 1
        else:
            end = middle - 1

    return False


def smallest_range(lists: List[List[int]]):
    """
    Time: O(n log n)
    Space: O(n)
    """

    unique_numbers = list({n for n in chain(*lists)})

    was_upper_bound_turn = True
    stop_upper_bound = False
    stop_lower_bound = False
    lower_range_bound_index = 0
    upper_range_bound_index = len(unique_numbers) - 1
    lower_range_bound = unique_numbers[lower_range_bound_index]
    upper_range_bound = unique_numbers[upper_range_bound_index]

    while lower_range_bound_index <= upper_range_bound_index:
        are_all_included = True
        for _list in lists:
            are_all_included &= included_in_range(
                _list, lower_range_bound, upper_range_bound
            )

        if not are_all_included:
            print(lower_range_bound, upper_range_bound)
            if was_upper_bound_turn:
                stop_upper_bound = True
            else:
                stop_lower_bound = True

        if was_upper_bound_turn:
            if stop_lower_bound:
                lower_range_bound_index -= 1
            else:
                lower_range_bound_index += 1
        else:
            if stop_upper_bound:
                upper_range_bound_index += 1
            else:
                upper_range_bound_index -= 1

        if stop_upper_bound and stop_lower_bound:
            break

        was_upper_bound_turn = not was_upper_bound_turn

        lower_range_bound = unique_numbers[lower_range_bound_index]
        upper_range_bound = unique_numbers[upper_range_bound_index]

    return [lower_range_bound, upper_range_bound]


if __name__ == "__main__":
    assert smallest_range(
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    ) == [20, 24]
