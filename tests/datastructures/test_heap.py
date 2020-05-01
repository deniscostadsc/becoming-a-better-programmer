import pytest

from datastructures import EmptyHeap, MinHeap


@pytest.fixture
def heap():
    return MinHeap()


def test_heap_size_is_initially_zero(heap):
    assert len(heap) == 0


def test_push_item_to_heap(heap):
    heap.push(1)
    assert len(heap) == 1


def test_push_item_that_should_be_replaced(heap):
    heap.push(2)
    heap.push(3)
    heap.push(4)
    heap.push(1)
    assert heap.peek() == 1
    assert heap._MinHeap__heap == [1, 2, 4, 3]


def test_heap_peek(heap):
    heap.push(1)
    assert heap.peek() == 1
    assert heap._MinHeap__heap == [1]


def test_peek_empty_heap(heap):
    with pytest.raises(EmptyHeap) as e:
        heap.peek()
    assert str(e.value) == "you cannot peek on empty heap"


def test_heap_pop(heap):
    heap.push(3)
    assert heap._MinHeap__heap == [3]
    assert len(heap) == 1
    assert heap.pop() == 3
    assert len(heap) == 0
    assert heap._MinHeap__heap == []


def test_pop_empty_heap(heap):
    with pytest.raises(EmptyHeap) as e:
        heap.pop()
    assert str(e.value) == "you cannot pop on empty heap"


def test_pop_item_and_check_heap_reorganization(heap):
    heap.push(10)
    heap.push(20)
    heap.push(15)
    heap.push(17)
    assert heap._MinHeap__heap == [10, 17, 15, 20]
    assert heap.pop() == 10
    assert len(heap) == 3
    assert heap.peek() == 15
    assert heap._MinHeap__heap == [15, 17, 20]


def test_pop_item_and_reorganize_and_should_stop_in_the_middle(heap):
    heap.push(10)
    heap.push(15)
    heap.push(20)
    heap.push(17)
    heap.push(16)
    assert heap._MinHeap__heap == [10, 15, 20, 17, 16]
    assert heap.pop() == 10
    assert len(heap) == 4
    assert heap.peek() == 15
    assert heap._MinHeap__heap == [15, 16, 20, 17]
