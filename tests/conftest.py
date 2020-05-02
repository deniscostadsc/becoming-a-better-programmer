import pytest


@pytest.helpers.register
def equal_items(expected, actual):
    return len(expected) == len(actual) and all(
        map(lambda x: x[0] == x[1], zip(actual, expected))
    )
