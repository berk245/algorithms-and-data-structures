# Linked List

## Definition

- Linked list is a linear data structure where each element in the list is contained in a seperate object, that is called a node which models two pieces of information:

  - The data that we want to store and
  - A reference to the next node in the list.

- The first node is called the head of the list, while the last node is called the tail. Every node other than the tail points to another node in the list.

- Since tail does not point to anything, that's how we know that's the end of the list.

- The list only keeps a reference to the head. In some implementations it keeps a reference to the tail as well.

- Linked lists come in two forms

  - Singly linked list: where each node stores a reference to the next node in the list
  - Doubly linked list: where each node stores a reference to the value before and after
    - Both implementations can be found in this repository.

- Linked lists are generally better in terms of inserting and removing elements when compared to arrays, since it is not necessary to shift the other values in case of insertion and deletion. However linked lists are bad at accessing (linear time) and since insertion and deletion requires a linear lookup, this advantage is not that significant at all times. In the following section, this will be explained in more detail.

## Common Operations and Their Time Complexities

1. Acces and Read Values = O(n)
   - Unlike arrays, linked lists do not index the elements within them. Therefore to be able to access and read a value, we have to go through each element that is before the element we are looking for.
   - In the worst case, we have to go through each element.
   - Therefore accessing and reading values take linear time and it is less addvantegous than array.
2. Search Values = O(n)
   - Similar to accessing a value, to search and find an element in a linked list, we have to go through each element until we find the value we are looking for.
   - This takes linear time, just as it does in an array.
3. Insert and Delete Values = O(1) for insert/delete, O(n) to access (depending on the position)
   - Insertion and deletion in theory are strengths of linked lists.
   - These operations require modification of only a few elements and are completed in constant time.
   - However this is only true if we are inserting the new values in the beginning of the list.
     - Or the end, if the linked list has a reference to the tail (see doubly_linked_list implementation)
   - The problem derives from the fact that for linked lists inserting data in any position is fast. But searching for that position to insert it is not (see point 2, it takes linear time)

## Strengths and Limitations

- The main advantage of linked lists over arrays is the dynamic sizing. The data structure does not require a contagious memory space and the programmer does not have to specify the size in initialization.
- The ease of insertion and deletion is another strength of linked list as it takes contant time to add a node to the head of the list. This advantage is less significant when this operation is done at a specific index, which requires going through elements.

- The main disadvantage of linked list is that it does not allow random access to elements. Usually the only reference that the list has is the head and to access any other element, we have to go through each element before it.
- Linked lists require each value to be bundled with at least one pointer, which means extra memory space.

## Real-world Use

- Linked lists are useful structures to build for learning purposes and are

- Some languages like Java already has linked list as built in data structures.

- The concepts that linked lists have can help programmers learn how to make tree based data structures and many other data structures.

- Any kind of use case that requires storage of previous and/or next data, or applications where insertions or deletions at random indexes are frequently made can make use of linked lists.
