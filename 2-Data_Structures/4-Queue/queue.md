# Queue

## Definition

- Queue is a linear data structure that stores values, that is similar to a stack
- Unlike stacks, queues operate in a First in First Out (FIFO) principle, which means that the least recently added item gets removed first.
- In Python, there are a number of ways to have queue features.
  - Using lists as queses
    - It is possible to use a list as a queue by making use of append() and pop(0) methods.
    - Append adds an item to the end of the list and pop(0) removes and returns the item in the first index.
    - Appending is a constant time operation. While removing the first element and unshifting each element by one is a linear time operation.
  - Implementiion with dequeue
    - Just like we did in stack implementation, we can use a double ended queue to implement a queue.
    - This implementation is preffered over lists since both adding an item to the end of the list and removing item from the start take constant time.
    - For enqueue and dequeue operations, append and popleft methods are used
  - Using Python built-in module Queue
    - Python has a built in module to implement queues as well.
    - This module is mainly for multi-producer, multi-consumer queues and it is especially useful in threaded programming when information must be exchanged safely between multiple threads.
  - In this repository, a custom Queue class is made based on dequeue module.

## Common Operations and Their Time Complexities

1. Enqueue = O(1)
   - Enqueue adds an item to the tail of the list.
   - Since the implementation is based on a linked list, this operation takes constant time.
2. Dequeue = O(1)
   - Dequeue returns the least recently added item from the queue and removes it.
   - This is a constant time operation.
   - If the queue is empty and underflow error occurs. In this implementation, an information string is printed while the method returns None.

## Strengths and Limitations

- A queue is a useful structure for any kind of scenario that requires First in First out principles.
- The enqueue and dequeue methods take constant time.
- Just as in stacks, queues are not designed to operate on the values that are in the middle or searching values.

## Real-world Use

- Queues have widespread uses in programming, especially for times when operations do not have to be processed immediately, but in a First in First out order.
- One important use of queues is CPU scheduling or Disk scheduling. When a resource has to be shared by different processes.
- Queues are also beneficial for operations that transfer data asynchronously. Some examples can be named as IO Buffers, pipes, file IO.
