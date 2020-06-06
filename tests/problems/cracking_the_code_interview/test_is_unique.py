from problems import has_unique_char


def test_has_unique_char():
    assert has_unique_char("a")


def test_has_not_unique_char():
    assert not has_unique_char("aa")
