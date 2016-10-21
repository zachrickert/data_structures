# -*- coding: utf-8 -*-
"""Testing module for the Heap classes."""

class Heap(object):
    """Heap class implementation"""
    def __init__(self, min_max='max'):
        """Initialize Heap"""
        self._heap = []
        self.size = 0
        heap_types = ['max', 'min']
        if min_max.lower() in heap_types:
            self._min_max = min_max.lower()
            if self._min_max == 'max':
                self._compare = self._compare_max
            else:
                self._compare = self._compare_min
        else:
            raise TypeError("heap needs either 'min' or 'max'")

    def insert(self, val):
        """Insert a node into the heap."""
        self._heap.append(val)
        current_position = self.size
        while current_position:
            # import pdb; pdb.set_trace()
            current_position = self._compare(current_position)
        self.size += 1

    def _compare_max(self, idx):
        """Compare a value with it's parent node, switches if needed."""
        parent = (idx - 1) >> 1
        if self._heap[idx] > self._heap[parent]:
            self._heap[idx], self._heap[parent] = self._heap[parent], self._heap[idx]
            return parent
        else:
            return 0

    def _compare_min(self, idx):
        """Compare a value with it's parent node, switches if needed."""
        parent = (idx - 1) >> 1
        if self._heap[idx] < self._heap[parent]:
            self._heap[idx], self._heap[parent] = self._heap[parent], self._heap[idx]
            return parent
        else:
            return 0

    def peak(self):
        """Peak at the first value in the heap."""
        return self._heap[0]
