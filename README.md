# data_structures
Repository for common data structures

## Singly Linked List
In computer science, a linked list is a linear collection of data elements, called nodes, each pointing to the next node by means of a pointer. 
[Linked list](https://en.wikipedia.org/wiki/Linked_list)
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

## Doubly Linked List
In computer science, a doubly linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains two fields, called links, that are references to the previous and to the next node in the sequence of nodes. The beginning and ending nodes' previous and next links, respectively, point to some kind of terminator, typically a sentinel node or null, to facilitate traversal of the list. 
[Doubly Linked list](https://en.wikipedia.org/wiki/Doubly_linked_list)
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
