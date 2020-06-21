from problems.cracking_the_code_interview.sorted_merge import sorted_merge


def test_sorted_merge():
    assert sorted_merge([1, -1], [2]) == [1, 2]
    assert sorted_merge([1, 3, -1, -1], [2, 4]) == [1, 2, 3, 4]
    assert sorted_merge([-1, -1], [2, 4]) == [2, 4]
    assert sorted_merge([1, 3, 5, 7, -1, -1, -1, -1], [2, 4, 6, 8]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
    ]
