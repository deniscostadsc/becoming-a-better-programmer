import pytest

from datastructures import LinkedList


@pytest.fixture
def linked_list():
    return LinkedList()


def test_linked_list_size_is_initially_zero(linked_list):
    assert len(linked_list) == 0


def test_append_item_to_linked_list(linked_list):
    linked_list.append(1)

    assert len(linked_list) == 1
    assert pytest.helpers.equal_items([1], linked_list)


def test_append_items_to_linked_list(linked_list):
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    assert len(linked_list) == 3
    assert pytest.helpers.equal_items([1, 2, 3], linked_list)


def test_prepend_items_to_linked_list(linked_list):
    linked_list.prepend(1)
    linked_list.prepend(2)
    linked_list.prepend(3)

    assert len(linked_list) == 3
    assert pytest.helpers.equal_items([3, 2, 1], linked_list)
