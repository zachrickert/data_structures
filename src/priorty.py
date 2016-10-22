# -*- coding: utf-8 -*-
"""Modules for the DLL Class and a Node Class that makes up the list."""

from heap import Heap


class PriortyQ(object):
    """Class implementation of a priorty queue."""

    def __init__(self):
        """Initialize the priorty queue."""
        self._queue = Heap()

    def insert(self, item, priorty=0):
        """
        Insert(item, priorty): inserts an item into the queue.
        with optional priorty.
        """
        pair = (priorty, item)
        self._queue.insert(pair)

    def pop(self):
        """pop(): removes the most important item from the queue."""
        priorty, item = self._queue.extract()
        return item

    def peak(self):
        """peek(): returns the most important item without removing it from the queue."""
        try:
            priorty, item = self._queue.peak()
        except TypeError:
            item = None
        return item

