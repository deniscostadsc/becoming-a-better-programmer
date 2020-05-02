import pytest

from datastructures import EmptyHeap, MinHeap


@pytest.fixture
def min_heap():
    return MinHeap()


def test_min_heap_size_is_initially_zero(min_heap):
    assert len(min_heap) == 0


def test_push_item_to_min_heap(min_heap):
    min_heap.push(1)
    assert len(min_heap) == 1


def test_push_item_to_min_that_should_be_replaced(min_heap):
    min_heap.push(2)
    min_heap.push(3)
    min_heap.push(4)
    min_heap.push(1)
    assert min_heap.peek() == 1
    assert pytest.helpers.equal_items([1, 2, 4, 3], min_heap)


def test_min_heap_peek(min_heap):
    min_heap.push(1)
    assert min_heap.peek() == 1
    assert pytest.helpers.equal_items([1], min_heap)


def test_peek_empty_min_heap(min_heap):
    with pytest.raises(EmptyHeap) as e:
        min_heap.peek()
    assert str(e.value) == "you cannot peek on empty heap"


def test_min_heap_pop(min_heap):
    min_heap.push(3)
    assert pytest.helpers.equal_items([3], min_heap)
    assert len(min_heap) == 1
    assert min_heap.pop() == 3
    assert len(min_heap) == 0
    assert pytest.helpers.equal_items([], min_heap)


def test_pop_empty_min_heap(min_heap):
    with pytest.raises(EmptyHeap) as e:
        min_heap.pop()
    assert str(e.value) == "you cannot pop on empty heap"


def test_pop_item_and_check_min_heap_reorganization(min_heap):
    min_heap.push(10)
    min_heap.push(20)
    min_heap.push(15)
    min_heap.push(17)
    assert pytest.helpers.equal_items([10, 17, 15, 20], min_heap)
    assert min_heap.pop() == 10
    assert len(min_heap) == 3
    assert min_heap.peek() == 15
    assert pytest.helpers.equal_items([15, 17, 20], min_heap)


def test_pop_item_and_heeck_min_heap_reorganization_again(min_heap):
    min_heap.push(10)
    min_heap.push(15)
    min_heap.push(20)
    min_heap.push(17)
    min_heap.push(16)
    assert pytest.helpers.equal_items([10, 15, 20, 17, 16], min_heap)
    assert min_heap.pop() == 10
    assert len(min_heap) == 4
    assert min_heap.peek() == 15
    assert pytest.helpers.equal_items([15, 16, 20, 17], min_heap)
