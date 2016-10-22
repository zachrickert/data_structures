# -*- coding: utf-8 -*-
"""Testing module for the Heap classes."""

from priorty import PriortyQ
import pytest
import random


# ------------------Heap Initialization Tests--------------------
# [x] Test default initialization of a priortyQ is a priortyQ.


def test_pq_initalization():
    """Test default initialization of a priortyQ is a priortyQ."""
    pq = PriortyQ()
    assert isinstance(pq, PriortyQ)


# ------------------Insert Method Tests--------------------
# [x] Insert one value into the heap check that value in heap.
# [x] Insert one value into the heap check at position 0.
# [x] Insert, insert bigger, greater priorty at position 0.
# [x] Insert, insert bigger, less priorty at position 1.

def test_pq_insert_one_item():
    """Insert one value into the heap check that value in priorty queue."""
    pq = PriortyQ()
    pq.insert("item", 1)
    assert (1, "item") in pq._queue._heap


def test_pq_insert_one_item_check_position():
    """Insert one value into the heap check at position 0."""
    pq = PriortyQ()
    pq.insert("item", 1)
    assert pq._queue._heap[0] == (1, "item")


def test_pq_insert_two_items_check_position0():
    """Insert one value into the heap check at position 0."""
    pq = PriortyQ()
    pq.insert("item", 1)
    pq.insert("item2", 2)
    assert pq._queue._heap[0] == (2, "item2")


def test_pq_insert_two_items_check_position1():
    """Insert one value into the heap check at position 0."""
    pq = PriortyQ()
    pq.insert("item", 1)
    pq.insert("item2", 2)
    assert pq._queue._heap[1] == (1, "item")


# ------------------Peak Method Tests--------------------
# [x] Insert one number, peak returns number
# [x] Insert multiple numbers, peak returns number with max priorty
# [x] Init priortyq, peak returns none.


def test_pq_peak_one_value():
    """Insert one number, peak returns number."""
    pq = PriortyQ()
    pq.insert("item", 1)
    assert pq.peak() == "item"


def test_peak_returns_max_priorty():
    """Insert multiple numbers, peak returns number with max priorty"""
    pq = PriortyQ()
    spots = 16
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        pq.insert(str(item), item)
    assert pq.peak() == str(max(sample_list))


def test_peak_returns_none_for_no_queue():
    """Init priortyq, peak returns none."""
    pq = PriortyQ()
    assert pq.peak() is None


# ------------------Pop Method Tests--------------------
# [x] Pop returns the head value.
# [x] Insert, insert, pop, check popped value.
# [x] Insert 3 values pop, check popped value is correct value
# [x] Priorty Queue still a heap after extraction.
# [x] Pop returns an IndexError if heap is empty.

def test_pop_returns_value():
    """Pop returns the head value."""
    pq = PriortyQ()
    pq.insert('item')
    assert pq.pop() == 'item'


def test_pop_returns_correct_value():
    """Insert, insert, pop, check popped value."""
    pq = PriortyQ()
    pq.insert('item', 1)
    pq.insert('item2', 2)
    assert pq.pop() == 'item2'


def test_insert3_pop_returns_correct_value():
    """Insert, insert, pop, check popped value."""
    pq = PriortyQ()
    pq.insert('item', 1)
    pq.insert('item3', 3)
    pq.insert('item2', 2)
    assert pq.pop() == 'item3'


def test_pop_still_heap_property():
    """Heap still a heap after extraction."""
    pq = PriortyQ()
    spots = 16
    sample_list = random.sample(range(100), spots)
    for item in sample_list:
        pq.insert(item, item)
    pq.pop()
    for idx, item in enumerate(pq._queue._heap):
        parent = max(0, (idx - 1) >> 1)
        assert pq._queue._heap[parent] >= pq._queue._heap[idx]


def test_pop_raises_index_error_if_no_queue():
    """Pop returns an IndexError if heap is empty."""
    pq = PriortyQ()
    with pytest.raises(IndexError):
        pq.pop()

