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


def test_insert_item_in_a_certain_position(linked_list):
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.insert(1, 6)

    assert len(linked_list) == 4
    assert pytest.helpers.equal_items([1, 6, 2, 3], linked_list)


def test_insert_item_on_empty_linked_list(linked_list):
    linked_list.insert(0, 6)

    assert len(linked_list) == 1
    assert pytest.helpers.equal_items([6], linked_list)


def test_raise_exception_when_index_is_out_of_range(linked_list):
    with pytest.raises(IndexError) as e:
        linked_list.insert(1, 6)

    assert str(e.value) == "linked-list index out of range"
    assert len(linked_list) == 0


def test_reverse_linked_list(linked_list):
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert pytest.helpers.equal_items([1, 2, 3], linked_list)
    linked_list.reverse()
    assert pytest.helpers.equal_items([3, 2, 1], linked_list)


def test_append_after_reverse_lisked_list(linked_list):
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert pytest.helpers.equal_items([1, 2, 3], linked_list)
    linked_list.reverse()
    assert pytest.helpers.equal_items([3, 2, 1], linked_list)
    linked_list.append(0)
    assert pytest.helpers.equal_items([3, 2, 1, 0], linked_list)


def test_prepend_after_reverse_lisked_list(linked_list):
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert pytest.helpers.equal_items([1, 2, 3], linked_list)
    linked_list.reverse()
    assert pytest.helpers.equal_items([3, 2, 1], linked_list)
    linked_list.prepend(0)
    assert pytest.helpers.equal_items([0, 3, 2, 1], linked_list)


def test_remove_node_from_linked_list(linked_list):
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    linked_list.remove(1)
    assert pytest.helpers.equal_items([6, 8], linked_list)


def test_remove_head_from_linked_list_and_then_prepend(linked_list):
    linked_list.append(6)
    linked_list.append(7)
    linked_list.remove(0)
    assert pytest.helpers.equal_items([7], linked_list)
    linked_list.prepend(5)
    assert pytest.helpers.equal_items([5, 7], linked_list)


def test_remove_tail_from_linked_list_and_then_append(linked_list):
    linked_list.append(6)
    linked_list.append(7)
    linked_list.remove(1)
    assert pytest.helpers.equal_items([6], linked_list)
    linked_list.append(5)
    assert pytest.helpers.equal_items([6, 5], linked_list)


def test_try_to_remove_out_of_index(linked_list):
    with pytest.raises(IndexError) as e:
        linked_list.remove(1)

    assert str(e.value) == "linked-list index out of range"
    assert len(linked_list) == 0
