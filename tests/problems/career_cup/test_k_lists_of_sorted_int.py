from problems.career_cup.k_lists_of_sorted_int import (
    included_in_range,
    smallest_range,
)


def test_included_in_range():
    assert included_in_range([4, 10, 15, 24, 26], lower_bound=0, upper_bound=26)
    assert not included_in_range(
        [4, 10, 15, 24, 26], lower_bound=27, upper_bound=29
    )
    assert included_in_range(
        [4, 10, 15, 24, 26], lower_bound=25, upper_bound=27
    )
    assert included_in_range(
        [4, 10, 15, 24, 26], lower_bound=20, upper_bound=24
    )
    assert included_in_range([0, 9, 12, 20], lower_bound=20, upper_bound=24)
    assert included_in_range([5, 18, 22, 30], lower_bound=20, upper_bound=24)


def test_k_lists_of_sorted_int():
    assert smallest_range(
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    ) == [20, 24]
    assert smallest_range([[1, 4, 9], [2, 4, 8], [2, 3, 4, 999]]) == [4, 4]
    assert smallest_range(
        [[1, 4, 10, 15, 24, 26], [0, 1], [2, 18, 22, 30]]
    ) == [1, 2]
