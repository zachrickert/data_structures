# -*- coding: utf-8 -*-
"""Testing module for the Doubly Linked List and Node classes."""

from queue import Queue
import pytest


# ------------------Queue Initialization Tests--------------------
# [x] test default initialization.

def test_queue_initalization():
    """Test default initialization."""
    queue = Queue()
    assert isinstance(queue, Queue)

# ------------------Enqueue Method Tests--------------------
# [x] enqueue(val), check first_node = val
# [x] enqueue(val),enqueue(val2), check first_node = val1
# [x] enqueue(val), enqueue(val2) check last_node = val2.

def test_enquque_val():
    """Enqueue(val), check first_node = val."""
    queue = Queue()
    anode = queue.enqueue('a')
    assert queue._queue.first_node is anode


def test_enquque_enqueue_check_first_node_val():
    """Enqueue(val), enqueue(val2) check first_node = val."""
    queue = Queue()
    anode = queue.enqueue('a')
    bnode = queue.enqueue('b')
    assert queue._queue.first_node is anode


def test_enquque_enqueue_check_last_node_val():
    """Enqueue(val), enqueue(val2) check last_node = val2."""
    queue = Queue()
    anode = queue.enqueue('a')
    bnode = queue.enqueue('b')
    assert queue._queue.last_node is bnode


# -------------Queue Initialization Tests by itterable---------------
# [x] initialize empty, first node is None.
# [x] initialize empty, last node is None.
# [x] initialize one charicter itterable, first node is val.
# [x] initialize two charicter itterable, first node is first char.
# [x] initialize two charicter itterable, last node is second char.

def test_initialization_with_empty_list_first_node_check():
    """Initialize empty, first node is None."""
    queue = Queue([])
    assert queue._queue.first_node is None


def test_initialization_with_empty_list_last_node_check():
    """Initialize empty, last node is None."""
    queue = Queue([])
    assert queue._queue.last_node is None


def test_initialization_with_list_first_node_val():
    """Initialize one charicter itterable, first node is val."""
    queue = Queue('a')
    assert queue._queue.first_node == 'a'


def test_initialization_with_two_items_first_node_val():
    """Initialize two charicter itterable, first node is first char."""
    queue = Queue('ab')
    assert queue._queue.first_node == 'a'


def test_initialization_with_two_items_last_node_val():
    """Initialize two charicter itterable, first node is first char."""
    queue = Queue('ab')
    assert queue._queue.last_node == 'b'

# ------------------Dequeue Method Tests--------------------
# [x] enqueue(val), dequeue = val
# [x] enqueue(val), dequeue = val, node is removed(last_node is None)
# [x] enqueue(val),enqueue(val2), dequeue = val
# [x] enqueue(val),enqueue(val2), dequeue = val, dequeue = val2
# [x] dequeue raises error
# [x] enqueue(val), dequeue = val, dequeue raises error


def test_dequeue_returns_value():
    """Enqueue(val), dequeue = val."""
    queue = Queue()
    queue.enqueue('a')
    assert queue.dequeue() is 'a'


def test_dequeue_removes_value():
    """Enqueue(val), dequeue = val, mode is removed(last_node is None)."""
    queue = Queue()
    queue.enqueue('a')
    queue.dequeue()
    assert queue._queue.last_node is None
    assert queue._queue.first_node is None


def test_values_dequeue_in_correct_order():
    """Enqueue(val),enqueue(val2), dequeue = val."""
    queue = Queue('ab')
    assert queue.dequeue() == 'a'


def test_values_dequeue_two_values_in_correct_order():
    """Enqueue(val),enqueue(val2), dequeue = val, dequeue = val2."""
    queue = Queue('ab')
    assert queue.dequeue() == 'a'
    assert queue.dequeue() == 'b'


def test_dequeue_empty_list_raises_error():
    """Dqueue raises error."""
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()


def test_queue_dequeue_dequeue_raises_error():
    """Enqueue(val), dequeue = val, dequeue raises error."""
    queue = Queue('a')
    queue.dequeue()
    with pytest.raises(IndexError):
        queue.dequeue()


# ------------------Peak Method Tests--------------------
# [x] enqueue(val), peak = val
# [x] enqueue(val), peak = val, node not removed(last_node is val)
# [x] enqueue(val),enqueue(val2), peak = val
# [x] peak empty returns none

def test_peak_returns_value():
    """Enqueue(val), peak = val."""
    queue = Queue('a')
    assert queue.peak() is 'a'


def test_peak_returns_value_does_not_dequeue():
    """Enqueue(val), peak = val, node not removed(last_node is val)."""
    queue = Queue('a')
    a = queue.peak()
    assert queue._queue.last_node == 'a'


def test_peak_returns_correct_value():
    """Enqueue(val),enqueue(val2), peak = val."""
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    assert queue.peak() is 'a'


def test_peak_empty_queue_returns_none():
    """Peak empty returns none."""
    queue = Queue()
    assert queue.peak() is None


# -------------Size Method Tests------------------
# [x] size of new queue is 0.
# [x] enqueue, size is 1.
# [x] enqueue, dequeue size is 0.
# [x] enqueue, peak size is 1.
# [x] dequeu, size of dll is 0.


def test_size_of_new_queue():
    """Size of new queue is 0."""
    queue = Queue()
    assert queue.size() == 0


def test_size_increments_with_enqueue():
    """Enqueue, size is 1."""
    queue = Queue()
    queue.enqueue('val')
    assert queue.size() == 1


def test_size_decrements_with_dequeue():
    """Enqueue, dequeue size is 0."""
    queue = Queue()
    queue.enqueue('val')
    assert queue.size() == 1
    queue.dequeue()
    assert queue.size() == 0


def test_size_stays_same_with_peak():
    """Enqueue, peak size is 1."""
    queue = Queue()
    queue.enqueue('val')
    assert queue.size() == 1
    queue.peak()
    assert queue.size() == 1


def test_size_stays_with_dequeue_error():
    """Dequeu, size of dll is 0."""
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()
    assert queue.size() == 0

