# Stack

## Definition

- A stack is an abstract data type that is a collection of elements.
- The name "stack" comes from the analogy to a set of physical items stacked on top of each other, like plates on a shelf.
- The two main operations a stack does are
  - Push: adding elements into the stack
  - Pop: removing the most recently added from the stack
- Stacks have a last-in-first-out principle. (LIFO)
- In Python, a stack can be implemented in different approaches:
  - Array / List:
    - We can create a custom stack structure, in which the container that holds the values is an array.
    - We then can append and pop the values into and out of the stack.
    - Since adding and removing an item to the end of the array takes constant time, these would be efficient operations.
    - However, the problem with this approach is the dynamic sizing of arrays and their contiguous memory principle.
    - If the stack container array exceeds its limits, it has to be allocated somewhere else in the memory with a bigger size and all the elements in the stack have to be copied.
    - This is an expensive operation and there are more efficient ways to implement a stack.
  - Linked list / Deque
    - A stack can be created based on a linked list.
    - Python has a data type called deque, or double-ended queue that is essentially a doubly-linked list, with the possibility to add and remove elements to the beginning and the end of the list.
    - Since these data types do not require a contiguous memory or a fixed size, they are more efficient bases to create a stack.
    - The implementation in this repository uses a deque for stack container.

## Common Operations and Their Time Complexities

1. Push = O(1)
   - Under the hood, push uses the append method, that adds the element to the end of the stack, or tail of the linked list.
   - Since none of the elements have to be shifted, this is a constant time operation.
   - Deque also allows adding elements to the head of the list with the appendleft method. This method is the same in terms of time complexity and could be used based on the programmer's choice.
2. Pop = O(1)
   - Pop returns the most recently added element and removes it from the stack.
   - Since only the pointers of the previous element have to be changed, this operation also takes constant time.
   - Just as the push method, pop can also be implemented to remove and return the head of the list. For that, the popleft method, which also has a constant time, can be used.
3. Peek = O(1)
   - Peek and pop are practically the same methods with one difference.
   - While pop takes out the most recently added value from the stack, after peek it still resides in the stack.
   - This method allows the programmer to read the latest addition into the stack, without any insertions or deletions.
   - Peek also has constant time complexity.
4. Search / Print = O(n)
   - In stacks, any operation that requires iterating on each element is expensive.
   - Some examples for those methods are searching for a value in the stack, printing the stack items, etc.

## Strengths and Limitations

- Stacks are convenient data structures for any problem that requires a last-in-first-out approach. Adding and removing the elements that are on top of the stack is fast and efficient.
- The limitation of stack appears when operations have to be made on the items which are in the middle of the stack. If an application requires a lot of random insertion, deletion, searching, and manipulating items in the list, a stack will probably not be the most efficient choice to implement.

## Real-world Use

- Stacks are useful data structures that are used in many areas.
- Some examples are:
  - The browsing history
  - Ctrl + z commands
- Moreover, calling a function in any programming language uses a stack to keep track of the variables and the calculations within the function.
