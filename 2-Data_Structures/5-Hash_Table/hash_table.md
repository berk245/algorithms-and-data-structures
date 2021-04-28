# Hash Table

## Definition

- A hash table, or a hash map, is a data structure that can map keys to values in a bucket array like structure.
- One of the fundamental parts of a hash table is the **hash function**, which computes an index from the key.
- This index is where the value would be stored or be found.
- There are different approaches to implement a hash function. In an ideal scenario, the hash function produces a unique index for each key, therefore each value is stored in a unique slot in the bucket array by its own.
- However most of the implemented hash functions may produce the same indexes for different keys. This is called a **collusion** and in order not to overwrite or loose data, a number of ways of approaches are used.
  1. Linear Probing / Open addressing
     - The linear probe approach solves the collusions by simply assigning the key value pair to the next available index.
     - During lookup, the hash function produces the index. The function then checks if the stored key in that index matches the provided key.
     - If yes. the value in that index is returned.
     - Otherwise, the get function starts iterating through the following key, value pairs until it finds the matching key.
  2. Seperate Chaining
     - This approach stores the list of key, value pairs in indexes, rather than storing the values themselves.
     - Using linked lists is a common practice for this approach.
     - When the hash table is initialized, the bucket array of max sized will be created with a linked list in each index.
     - When an index is created for insertion, the add method will simply add the key-value pair to the linked list.
     - On the lookup, the function will iterate over the items of the linked list in the index produced by the hash function.
  - In this repository, implementation of both of the above mentioned approaches can be found. For easier demonstration, seperate chaining uses a normal array (Python list) instead of a linked list.
    - Since the new key-value pairs are appended to the end of the list, the only disadvantage of this implemetation is the dynamic sizing of an array.
  - The implemetations have a hash function that always return 1. This is an intentional decision to demonstrate the worst case scenarios (will be discussed in the next section).

## Common Operations and Their Time Complexities

1. Lookup by key / Delete = Average O(1) / Worst case O(n)
   - In a well implemeted hash table, the average time complexity of a lookup is constant and independent from the number of elements stored in the hash table.
   - However, in case of collusions, this complexity may increase in reality.
   - The worst case scenario happens when the hash function produces the same index when inserting. Depending on the collusion resolving approach that is used, the get function has to go look either the next slots in the bucket array or in the linked list until it finds the matching key.
     - In such cases, the upper bound time complexity is O(n)
2. Insert = Average O(1) / Worst case O(n)
   - Insertion of key value pairs take constant time on average.
   - The worst case occurs with open addressing collusion resolution and a bad hash function that is described above.
     - In such cases, in order to place the key value pair, it is necessary to go over each element until there is a free address.
     - Therefore it takes linear time, O(n) in the worst case scenario.

## Strengths and Limitations

- Hash tables' main advantage over the table data structures is speed, especially in larger sizes.
- Hash tables are particularly efficient when the max size is known or can be predicted, since the bucket array can be allocated and never have to beresized
- Although operations on hash table is significantly fast, it still requires the services of a hash function, which if implemented well can be a costly operation. Therefore for smaller number of entries, this cost may be inefficient.
- Additionally hash tables become quite inefficient when there are many collusions.

## Real-world Use

- Many programming languages provide hash table functionality either by built-in features or by libraries.
- Therefore it is unlikely that a programmer has to implemet their own hash table class. However it is beneficial to understand how they work.
- Hash tables are used to implement associative arrays, whose indices are arbitrary strings or other complicated objects (like dictionary in Python or an object in JS). They are also used in database indexing, implementing caches and set data structure.
