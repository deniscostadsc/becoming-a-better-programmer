from problems.cracking_the_code_interview.is_unique import (
    is_unique,
    is_unique_with_no_additional_datastructures,
)


def test_all_chars_are_unique():
    assert is_unique("a")
    assert is_unique("abcde")


def test_has_repeated_chars():
    assert not is_unique("aa")
    assert not is_unique("abccde")


def test_has_only_unique_chars_with_no_additional_datastructures():
    assert is_unique_with_no_additional_datastructures("a")
    assert is_unique_with_no_additional_datastructures("abc")
    assert is_unique_with_no_additional_datastructures("abcd")
    assert is_unique_with_no_additional_datastructures("abcde")


def test_has_repeated_chars_with_no_additional_datastructures():
    assert not is_unique_with_no_additional_datastructures("aa")
    assert not is_unique_with_no_additional_datastructures("aac")
    assert not is_unique_with_no_additional_datastructures("abccde")
    assert not is_unique_with_no_additional_datastructures("caa")
