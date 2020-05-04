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


def test_append_items_to_linked_list(linked_list):
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert len(linked_list) == 3
