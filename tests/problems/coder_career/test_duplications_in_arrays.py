from problems.coder_career.duplications_in_arrays import duplications_in_arrays


def test_duplications_in_arrays():
    assert duplications_in_arrays([1, 1, 1, 4, 4]) == [1, 4]
    assert duplications_in_arrays([1, 1, 3, 4, 1]) == [1]
    assert duplications_in_arrays([1, 2, 2]) == [2]
    assert duplications_in_arrays([1, 2, 3, 4, 1]) == [1]
    assert duplications_in_arrays([1, 2, 3, 4, 5, 5]) == [5]
    assert duplications_in_arrays([1, 2, 3, 4, 5, 6, 6]) == [6]
    assert duplications_in_arrays([2, 3, 5, 4, 3, 2, 6, 7]) == [2, 3]
