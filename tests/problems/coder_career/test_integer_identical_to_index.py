from problems.coder_career.integer_identical_to_index import identical_to_index


def test_integer_identical_to_index():
    assert identical_to_index([0]) == 0
    assert identical_to_index([-1, 1]) == 1
    assert identical_to_index([-3, -1, 1, 3, 5]) == 3
    assert identical_to_index([-3, -1, 1, 2, 4]) == 4
    assert identical_to_index([0, 2, 3, 4, 5, 6]) == 0
