from problems import (
    has_unique_char,
    has_unique_char_with_no_additional_datastructures,
)


def test_has_only_unique_chars():
    assert has_unique_char("a")
    assert has_unique_char("abcde")


def test_has_repeated_chars():
    assert not has_unique_char("aa")
    assert not has_unique_char("abccde")


def test_has_only_unique_chars_with_no_additional_datastructures():
    assert has_unique_char_with_no_additional_datastructures("a")
    assert has_unique_char_with_no_additional_datastructures("abc")
    assert has_unique_char_with_no_additional_datastructures("abcd")
    assert has_unique_char_with_no_additional_datastructures("abcde")


def test_has_repeated_chars_with_no_additional_datastructures():
    assert not has_unique_char_with_no_additional_datastructures("aa")
    assert not has_unique_char_with_no_additional_datastructures("aac")
    assert not has_unique_char_with_no_additional_datastructures("abccde")
    assert not has_unique_char_with_no_additional_datastructures("caa")
