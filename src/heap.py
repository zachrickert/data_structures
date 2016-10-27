# -*- coding: utf-8 -*-
"""Testing module for the Heap classes."""


class Heap(object):
    """Heap class implementation."""

    def __init__(self, min_max='max'):
        """Initialize Heap."""
        self._heap = []
        self.size = 0
        heap_types = ['max', 'min']
        if min_max.lower() in heap_types:
            self._min_max = min_max.lower()
            if self._min_max == 'max':
                self._shift_up = self._shift_up_max
                self._shift_down = self._shift_down_max
            else:
                self._shift_up = self._shift_up_min
                self._shift_down = self._shift_down_min
        else:
            raise TypeError("heap needs either 'min' or 'max'")

    def insert(self, val):
        """Insert a node into the heap."""
        self._heap.append(val)
        current_position = self.size
        while current_position:
            # import pdb; pdb.set_trace()
            current_position = self._shift_up(current_position)
        self.size += 1

    def _shift_up_max(self, idx):
        """Shift a value with it's parent node, switches if needed."""
        parent = (idx - 1) >> 1
        if self._heap[idx] > self._heap[parent]:
            self._heap[idx], self._heap[parent] = self._heap[parent], self._heap[idx]
            return parent
        else:
            return 0

    def _shift_up_min(self, idx):
        """Shift a value with it's parent node, switches if needed."""
        parent = (idx - 1) >> 1
        if self._heap[idx] < self._heap[parent]:
            self._heap[idx], self._heap[parent] = self._heap[parent], self._heap[idx]
            return parent
        else:
            return 0

    def peak(self):
        """Peak at the first value in the heap."""
        try:
            return self._heap[0]
        except IndexError:
            # No heap exisits.
            return None

    def extract(self):
        """Extract top node in the heap."""
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        val = self._heap.pop()
        self.size -= 1
        current_position = 0
        while True:
            new_position = self._shift_down(current_position)
            if new_position == current_position:
                break
            current_position = new_position
        return val

    def _shift_down_max(self, idx):
        child1 = (2 * idx) + 1
        child2 = (2 * idx) + 2

        try:
            value1 = _get_first_item(self._heap[child1])
        except IndexError:
            return idx
        try:
            value2 = _get_first_item(self._heap[child2])
        except IndexError:
            value2 = float('-inf')

        value_idx = _get_first_item(self._heap[idx])

        if value1 >= value2:
            if value1 > value_idx:
                self._heap[child1], self._heap[idx] = self._heap[idx], self._heap[child1]
                return child1
            else:
                return idx
        else:
            if value2 > value_idx:
                self._heap[child2], self._heap[idx] = self._heap[idx], self._heap[child2]
                return child2
            else:
                return idx

    def _shift_down_min(self, idx):
        child1 = (2 * idx) + 1
        child2 = (2 * idx) + 2

        try:
            value1 = _get_first_item(self._heap[child1])
        except IndexError:
            return idx
        try:
            value2 = _get_first_item(self._heap[child2])
        except IndexError:
            value2 = float('inf')

        value_idx = _get_first_item(self._heap[idx])

        if value1 <= value2:
            if value1 < value_idx:
                self._heap[child1], self._heap[idx] = self._heap[idx], self._heap[child1]
                return child1
            else:
                return idx
        else:
            if value2 < value_idx:
                self._heap[child2], self._heap[idx] = self._heap[idx], self._heap[child2]
                return child2
            else:
                return idx

def _get_first_item(value):
        """
        Helper function allows tuples and lists to be ordered.
        Ordering based on their first value.
        """
        if isinstance(value, (list, tuple)):
            return value[0]
        else:
            return value
