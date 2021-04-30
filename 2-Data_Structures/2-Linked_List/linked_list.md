# Linked List

## Definition

- Linked list is a linear data structure where each element in the list is contained in a separate object, called a node, which models two pieces of information:

  - The data that we want to store and
  - A reference to the next node in the list.

- The first node is called the head of the list, while the last node is called the tail. Every node other than the tail points to another node in the list.

- The end of the list is signified by the node that does not point to the next node. (the tail)
- The list only keeps a reference to the head. In some implementations, it keeps a reference to the tail as well.

- Linked lists come in two forms

  - Singly-linked list: where each node stores a reference to the next node in the list
  - Doubly-linked list: where each node stores a reference to the value before and after
    - Both implementations can be found in this repository.

- Linked lists generally perform better than arrays when inserting and removing items.
- The main reason for that it is not necessary to shift the other values in case of insertion and deletion.
- However, linked lists are bad at accessing items. (linear time)
- Since insertion and deletion require a linear lookup, this advantage is not that significant at all times. In the following section, this will be explained in more detail.

## Common Operations and Their Time Complexities

1. Acces and Read Values = O(n)
   - Unlike arrays, linked lists do not index the items they contain. Therefore, we have to go through each node in the list until we find the one we are looking for.
   - In the worst case, we have to go through each item or node.
   - Therefore, accessing or reading values takes linear time.
2. Search Values = O(n)
   - To search and find a value in a linked list, we have to go through each node until we find the value we are looking for.
   - Similar to an array, searching operations take linear time.
3. Insert and Delete Values = O(1) for insert/delete, O(n) to access (depending on the position)
   - In theory, insertion and deletion are strengths of linked lists.
   - These operations require modification of only a few elements and are completed in constant time.
   - However, this is only true if we insert the new values at the beginning of the list.
     - This applies to the insertions at the end when the linked list has a reference to the tail. (see doubly_linked_list implementation)
   - The problem derives from the fact that for linked lists inserting data in any position is fast. But searching for that position to insert it is not (see point 2, it takes linear time)

## Strengths and Limitations

- The main advantage of linked lists over arrays is the un-fixed sizing. The data structure does not require a contagious memory space. Additionally, the programmer does not have to specify the size during the initialization.
- The ease of insertion and deletion is another strength of a linked list as it takes constant time to add a node to the head of the list. This advantage is less significant when this operation is done at a specific index, which requires going through elements.

- The main disadvantage of a linked list is that it does not allow random access to elements. Usually, the only reference that the list has is the head, and to access any other item, we have to go through each item before it.
- Linked lists require each value to be bundled with at least one pointer, which means extra memory space.

## Real-world Use

- Linked lists are helpful structures to build, especially for learning purposes.

- Some languages like Java already have linked lists as built-in data structures.

- The concepts that linked lists have can help programmers learn how to make tree-based data structures and many other data structures.

- In use cases that require the storage of the previous or the following data, or applications where insertions or deletions at random indexes are frequent can make use of linked lists.
