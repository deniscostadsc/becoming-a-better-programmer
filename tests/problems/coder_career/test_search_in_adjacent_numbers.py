import pytest

from problems.coder_career.search_in_adjacent_numbers import (
    search_in_adjacent_numbers,
)


def test_search_in_adjacent_numbers():
    assert search_in_adjacent_numbers([1, 2, 1, 2, 3, 4, 3, 4, 5], 3) == 4
    assert search_in_adjacent_numbers([5, 4, 3, 2, 1], 1) == 4
    assert search_in_adjacent_numbers([1, 2, 1], 1) == 0
    assert search_in_adjacent_numbers([1], 1) == 0
    assert search_in_adjacent_numbers([4, 5, 6, 5, 6, 7, 8, 9, 10, 9], 9) == 7


def test_search_in_adjacent_numbers_not_in_list():
    with pytest.raises(ValueError) as e:
        search_in_adjacent_numbers([1, 2, 1], 3)
    assert str(e.value) == "3 is not in list"

    with pytest.raises(ValueError) as e:
        search_in_adjacent_numbers([1, 2, 1], 6)
    assert str(e.value) == "6 is not in list"
