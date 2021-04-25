# Stack

## Definition

- A stack is an abstract data type that is a collection of elements.
- The name "stack" for this type of structure comes from the analogy to a set of physical items stacked on top of each other, like plates on a shelf.
- The two main operations a stack does are
  - Push: adding elements into the stack
  - Pop: removing the most recently added from the stack
- Stacks have a 'Last in first out' principle. (LIFO)
- In Python, a stack can be implemented in different approaches:
  - Array / List:
    - We can create a custom stack structure, in which the container that holds the values is an array.
    - We then can append and pop the values into and out of the stack.
    - Since adding and removing an element to the and of the array takes constant time, these would be efficient operations.
    - However, the problem with this approach is the dynamic sizing of arrays and their contigious memory principle.
    - If there are more elements in the stack than the array size, the array has to be allocated somewhere else in the memory with a bigger size and all the elements in the stack have to copied.
    - This is an expensive operation. Therefore there are more efficient ways to implement a stack.
  - Linked list / Deque
    - A stack can be created based on a linked list.
    - Python has a data type called deque, or double-ended queue that is essentially a doubly linked list, with the possibilty to add and remove elements to the beginning and the end of the list.
    - Since these data types do not require a contigious memory or a fixed size, they are more efficient bases to create a stack.
    - The implementation in this repository uses a deque for stack container.

## Common Operations and Their Time Complexities

1. Push = O(1)
   - Under the hood, push uses the append method, that adds the element to the end of the stack, or tail of the linked list.
   - Since none of the elements have to be shifted, this is a constant time operation.
   - Deque also allows adding elements as the head of the list with appendleft method. This method is the same in terms of time complexity and could be used based on the programmers choice.
2. Pop = O(1)
   - Pop returns the most recently added element from the stack and removes it.
   - Since only the pointers of the previous element has to be cahnged, this operation also takes constant time.
   - Just as the push method, pop can also be implemented to take out and return the head of the list. For that, popleft method, which also has a constant time can be used.
3. Peek = O(1)
   - Peek and pop are practically same methods with one differnece.
   - While after pop the most recently added value is taken out from the stack, after peek it still resides in the stack.
   - This methods allows us to read the latest addition into the stack.
   - Peek also has a constant time complexity.
4. Search / Print = O(n)
   - In stacks, any operation that requires iterating on each element is expensive.
   - Some examples for those methods are searching for a value in the stack, inserting/removing a value that is in the middle of the stack, pronting the elements of the stack.

## Strengths and Limitations

- Stacks are convenient data structres for any problem that requires a Last in First out approach. Adding and removing the elements that are on top of the stack is fast and efficient.
- The limitation of stack appears when operations have to be made on the elements that are in the middle of stack. If an application requires a lot of random insertion, deletion, search etc, stack will probably not be the most efficient choice to implement.

## Real-world Use

- Stacks are useful data structures that are used in many areas.
- Some examples can be named as:
  - The browsing history
  - Ctrl + z commands
- Moreover calling a function in any progrqamming language uses a stack to keep track of the variables and the calculations within the function.
