# data_structures
Repository for common data structures

## [Singly Linked list](https://en.wikipedia.org/wiki/Linked_list)
In computer science, a linked list is a linear collection of data elements, called nodes, each pointing to the next node by means of a pointer. 

This linked list will include the following operations:
* push(val) - will insert the value ‘val’ at the head of the list
* pop() - will pop the first value off the head of the list and return it.
* size() - will return the length of the list
* search(val) - will return the node containing ‘val’ in the list,
    if present, else None
* remove(val) - will remove the given node from the list, 
    wherever it might be (node must be an item in the list)
* traverse(start, end) - will traverse through the list with given start and end nodes.
    start - default set to the head of the list.
    end - will run until end node is reached.  default set to the end of the list. 
        if end node is before the start node it will  
* display() - will return a unicode string representing the list 
    as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”

## [Doubly Linked list](https://en.wikipedia.org/wiki/Doubly_linked_list)
In computer science, a doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains two fields, called links, that are references to the previous and to the next node in the sequence of nodes. The beginning and ending nodes' previous and next links, respectively, point to some kind of terminator, typically a sentinel node or null, to facilitate traversal of the list. 

This doubly linked list will have these operations:
* push(val) will insert the value ‘val’ at the head of the list
* append(val) will append the value ‘val’ at the tail of the list
* size() - will return the length of the list
* pop() will pop the first value off the head of the list and return it.
* shift() will remove the last value from the tail of the list and return it.
* search(val) - will return the node containing ‘val’ in the list,
    if present, else None
* remove(val) will remove the first instance of ‘val’ found in the list, starting from the head. If ‘val’ is not present, it will raise an appropriate Python exception.
* traverse_forward() - Traverse from the first node going forward through the list.
* traverse_backward() - Traverse from the last node going reverse through the list.
* insert_after(val, node) - Insert a node after a given node.
* insert_before(val, node) - Insert a node before a given node.

##[Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))
In computer science, a queue is a particular kind of abstract data type or collection in which the entities in the collection are kept in order and the principal (or only) operations on the collection are the addition of entities to the rear terminal position, known as enqueue, and removal of entities from the front terminal position, known as dequeue. 

This queue will have the following operations:
* enqueue(value): adds value to the queue
* dequeue(): removes the correct item from the queue and returns its value (should raise an error if the queue is empty)
* peek(): returns the next value in the queue without dequeueing it. If the queue is empty, returns None
* size(): return the size of the queue. Should return 0 if the queue is empty.

##[Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
In computer science, a stack is an abstract data type that serves as a collection of elements, with two principal operations: push, which adds an element to the collection, and pop, which removes the most recently added element that was not yet removed. The order in which elements come off a stack gives rise to its alternative name, LIFO (for last in, first out). Additionally, a peek operation may give access to the top without modifying the stack.

This stack will have the following operations:
* push(value): adds value to the stack
* pop(): removes the correct item from the queue and returns its value (should raise an error if the stack is empty)
* peek(): returns the first value in the stack without removing it. If the stack is empty, returns None
* size(): return the size of the stack. Should return 0 if the stack is empty.

##[Deque](https://en.wikipedia.org/wiki/Double-ended_queue)
In computer science, a double-ended queue (dequeue, often abbreviated to deque, pronounced deck) is an abstract data type that generalizes a queue, for which elements can be added to or removed from either the front (head) or back (tail)

This deque will have the following operstions:
* append(val): appends a value to the end of the deque.
* append_left(val): appends a value to the front of the deque.
* pop(): pops a value off of the end of the deque.
* pop_left(): pops a value off the beginning of the deque.
* peak(): returns the last value in the deque without removing it. If the stack is empty, returns None
* peak_left(): returns the first value in the deque without removing it. If the stack is empty, returns None
* size(): return the size of the deque. Should return 0 if the deque is empty.

