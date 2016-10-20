# -*- coding: utf-8 -*-
"""Modules for the DLL Class and a Node Class that makes up the list."""

from double import DLL


class Queue(object):
    """class implementation of a Queue."""

    def __init__(self, itterable=None):
        """Initialize the queue."""
        self._queue = DLL(itterable)

    def enqueue(self, val):
        """Enqueue an item, push onto the first node."""
        return self._queue.append(val)

    def dequeue(self):
        """
        Dequeue first item in list.

        Remove the correct item from the queue and returns its value.
        (should raise an error if the queue is empty)
        """
        return self._queue.pop()

    def peak(self):
        """
        Peak at next item to be dequeue.

        Return the next value in the queue without dequeueing it.
        If the queue is empty, returns None
        """
        try:
            return self._queue.first_node.value
        except AttributeError:
            # Attribute error is first_node is None
            return None

    def size(self):
        """Return size of the queue."""
        return self._queue.size()

