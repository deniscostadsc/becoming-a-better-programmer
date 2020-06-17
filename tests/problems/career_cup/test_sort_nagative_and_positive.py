from problems.career_cup.sort_negative_and_positive import (
    sort_negative_and_positive,
)


def test_sort_positive_and_negative():
    assert sort_negative_and_positive([-1]) == [-1]
    assert sort_negative_and_positive([1, -1]) == [-1, 1]
    assert sort_negative_and_positive([1, -2, 1]) == [-2, 1, 1]
    assert sort_negative_and_positive([-1, 0, -1]) == [-1, -1, 0]
    # assert sort_negative_and_positive([-1, 1, 3, -2, 2]) == [-1, -2, 1, 3, 2]
