# -*- coding: utf-8 -*-
"""Testing module for the Heap classes."""

from heap import Heap
import pytest
import random


# ------------------Heap Initialization Tests--------------------
# [x] Test default initialization of a heap is a heap.
# [x] Test the inital size of a heap is 0.
# [x] Test the default initializtion is a max heap.
# [x] Test the override to a min heap.
# [x] Test if invalid input into min/max heap results in an error.

def test_heap_initalization():
    """Test default initialization of a heap is a heap."""
    heap = Heap()
    assert isinstance(heap, Heap)


def test_heap_size_initally_0():
    """Test the inital size of a heap is 0."""
    heap = Heap()
    assert heap.size == 0


def test_heap_init_default_max():
    """Test the default initializtion is a max heap."""
    heap = Heap()
    assert heap._min_max == 'max'


def test_heap_init_override_min():
    """Test the override to a min heap."""
    heap = Heap('min')
    assert heap._min_max == 'min'


def test_heap_init_error_on_unknown_type():
    """Test the init throws an error if given unknown type."""
    with pytest.raises(TypeError):
        heap = Heap('blah')

# ------------------Insert Method Tests--------------------
# [x] Insert one value into the heap check that value in heap.
# [x] Insert one value into the heap check at position 0.
# [x] Insert one value, size increases.
# [x] Insert, insert smaller, value at position 1.
# [x] Insert, insert bigger, value at position 0.
# [x] Minheap, insert, insert smaller, value at position 1.
# [x] Minheap, Insert, insert bigger, value at position 0.
# [x] Insert random nodes, verify heap property
# [x] Minheap insert random nodes, verify heap property


def test_insert_one_value_in_heap():
    """Insert one value into the heap check that value in heap."""
    heap = Heap()
    heap.insert(10)
    assert 10 in heap._heap


def test_insert_one_value_at_position_0():
    """Insert one value into the heap check at position 0."""
    heap = Heap()
    heap.insert(10)
    assert heap._heap[0] == 10


def test_insert_increases_size():
    """Insert one value, size increases."""
    heap = Heap()
    assert heap.size == 0
    heap.insert(10)
    assert heap.size == 1


def test_insert_two_values_check_position_two():
    """Insert, insert smaller, value at position 1."""
    heap = Heap()
    heap.insert(10)
    heap.insert(7)
    assert heap._heap[1] == 7


def test_insert_two_values_check_position_two_switch_positions():
    """Insert, insert bigger, value at position 0."""
    heap = Heap()
    heap.insert(7)
    heap.insert(10)
    assert heap._heap[0] == 10


def test_min_insert_two_values_check_position_two():
    """Minheap, Insert, insert smaller, value at position 1."""
    heap = Heap('min')
    heap.insert(10)
    heap.insert(7)
    assert heap._heap[0] == 7


def test_min_insert_two_values_check_position_two_switch_positions():
    """MinHeap, Insert, insert bigger, value at position 0."""
    heap = Heap('min')
    heap.insert(7)
    heap.insert(10)
    assert heap._heap[1] == 10


def test_insert_follows_heap_property():
    """Insert random nodes, verify heap property."""
    heap = Heap()
    spots = 16
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        heap.insert(item)
    for idx, item in enumerate(heap._heap):
        parent = max(0, (idx - 1) >> 1)
        assert heap._heap[parent] >= heap._heap[idx]


def test_minheap_insert_follows_heap_property():
    """Insert random nodes, verify heap property."""
    heap = Heap('min')
    spots = 16
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        heap.insert(item)
    for idx, item in enumerate(heap._heap):
        parent = max(0, (idx - 1) >> 1)
        assert heap._heap[parent] <= heap._heap[idx]


# ------------------Peak Method Tests--------------------
# [x] Insert one number, peak returns number
# [x] Insert multiple numbers, peak returns max
# [x] Minheap - Insert multiple numbers, peak returns min
# [x] Init heap, peak returns none.

def test_peak_heap_of_one_item():
    """Insert one number, peak returns number."""
    heap = Heap()
    heap.insert(10)
    assert heap.peak() == 10


def test_peak_returns_max():
    """Insert multiple numbers, peak returns max."""
    heap = Heap()
    spots = 16
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        heap.insert(item)
    assert heap.peak() == max(sample_list)


def test_peak_returns_min():
    """Insert multiple numbers, peak returns max."""
    heap = Heap('min')
    spots = 16
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        heap.insert(item)
    assert heap.peak() == min(sample_list)


def test_peak_no_heap():
    """Init heap, peak returns none."""
    heap = Heap()
    assert heap.peak() is None


# ------------------Extract Method Tests--------------------
# [x] Extract returns the head value.
# [x] Insert, insert, extract, check first value.
# [x] Insert 3 values extract, check first value is correct value
# [x] Minheap Insert 3 values extract, check first value is correct value
# [x] Heap still a heap after extraction.
# [x] Minheap still a min heap after extraction.
# [x] Extract returns an IndexError if heap is empty.
# [x] Extract decrements the size of the heap.


def test_extract_returns_value():
    """Extract returns the head value."""
    heap = Heap()
    heap.insert(10)
    assert heap.extract() == 10


def test_extract_moves_next_value_to_top():
    """Insert, insert, extract, check first value."""
    heap = Heap()
    heap.insert(10)
    heap.insert(7)
    heap.extract()
    assert heap.extract() == 7


def test_extract_moves_correct_value_to_top():
    """Insert 3 values extract, check first value is correct value."""
    heap = Heap()
    heap.insert(5)
    heap.insert(7)
    heap.insert(10)
    assert heap.extract() == 10
    assert heap.extract() == 7
    assert heap.extract() == 5


def test_minheap_extract_moves_correct_value_to_top():
    """Minheap Insert 3 values extract, check first value is correct value."""
    heap = Heap('min')
    heap.insert(10)
    heap.insert(7)
    heap.insert(5)
    assert heap.extract() == 5
    assert heap.extract() == 7
    assert heap.extract() == 10


def test_extract_still_heap_property():
    """Heap still a heap after extraction."""
    heap = Heap()
    spots = 16
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        heap.insert(item)
    heap.extract()
    for idx, item in enumerate(heap._heap):
        parent = max(0, (idx - 1) >> 1)
        assert heap._heap[parent] >= heap._heap[idx]


def test_extract_still_minheap_property():
    """Heap still a minheap after extraction."""
    heap = Heap('min')
    spots = 16
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        heap.insert(item)
    heap.extract()
    for idx, item in enumerate(heap._heap):
        parent = max(0, (idx - 1) >> 1)
        assert heap._heap[parent] <= heap._heap[idx]


def test_extract_from_empty_heap():
    """Extract returns an IndexError if heap is empty."""
    heap = Heap()
    with pytest.raises(IndexError):
        heap.extract()


def test_extract_decrements_size_of_heap():
    """Extract decrements the size of the heap."""
    heap = Heap()
    heap.insert(10)
    heap.insert(7)
    assert heap.size == 2
    heap.extract()
    assert heap.size == 1

# ------------------Overall Tests--------------------
# [x] Add values to heap, extract values. Chek all in order.
# [] Add values to minheap, extract values. Chek all in order.


def test_overall_heap_function():
    """Add values to heap, extract values. Chek all in order."""
    heap = Heap()
    spots = 32
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        heap.insert(item)
    last_item = heap.extract()
    while heap.size > 0:
        new_item = heap.extract()
        assert new_item <= last_item
        last_item = new_item


def test_overall_minheap_function():
    """Add values to minheap, extract values. Chek all in order."""
    heap = Heap('min')
    spots = 32
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        heap.insert(item)
    last_item = heap.extract()
    while heap.size > 0:
        new_item = heap.extract()
        assert new_item >= last_item
        last_item = new_item

