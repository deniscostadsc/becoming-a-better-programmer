import pytest

from datastructures import EmptyHeap, MaxHeap


@pytest.fixture
def max_heap():
    return MaxHeap()


def test_max_heap_size_is_initially_zero(max_heap):
    assert len(max_heap) == 0


def test_push_item_to_max_heap(max_heap):
    max_heap.push(1)
    assert len(max_heap) == 1


def test_push_item_to_max_that_should_be_replaced(max_heap):
    max_heap.push(2)
    max_heap.push(3)
    max_heap.push(4)
    max_heap.push(1)
    assert max_heap.peek() == 4
    assert pytest.helpers.equal_items([4, 2, 3, 1], max_heap)


def test_max_heap_peek(max_heap):
    max_heap.push(1)
    assert max_heap.peek() == 1
    assert pytest.helpers.equal_items([1], max_heap)


def test_peek_empty_max_heap(max_heap):
    with pytest.raises(EmptyHeap) as e:
        max_heap.peek()
    assert str(e.value) == "you cannot peek on empty heap"


def test_max_heap_pop(max_heap):
    max_heap.push(3)
    assert pytest.helpers.equal_items([3], max_heap)
    assert len(max_heap) == 1
    assert max_heap.pop() == 3
    assert len(max_heap) == 0
    assert pytest.helpers.equal_items([], max_heap)


def test_pop_empty_max_heap(max_heap):
    with pytest.raises(EmptyHeap) as e:
        max_heap.pop()
    assert str(e.value) == "you cannot pop on empty heap"


def test_pop_item_and_check_max_heap_reorganization(max_heap):
    max_heap.push(10)
    max_heap.push(20)
    max_heap.push(15)
    max_heap.push(17)
    assert pytest.helpers.equal_items([20, 17, 15, 10], max_heap)
    assert max_heap.pop() == 20
    assert len(max_heap) == 3
    assert max_heap.peek() == 17
    assert pytest.helpers.equal_items([17, 10, 15], max_heap)


def test_pop_item_and_check_max_heap_reorganization_again(max_heap):
    max_heap.push(20)
    max_heap.push(17)
    max_heap.push(10)
    max_heap.push(15)
    max_heap.push(16)
    assert pytest.helpers.equal_items([20, 17, 10, 15, 16], max_heap)
    assert max_heap.pop() == 20
    assert len(max_heap) == 4
    assert max_heap.peek() == 17
    assert pytest.helpers.equal_items([17, 16, 10, 15], max_heap)
