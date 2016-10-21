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
# [] Minheap - Insert multiple numbers, peak returns min
# [] Init heap, peak returns none.

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


