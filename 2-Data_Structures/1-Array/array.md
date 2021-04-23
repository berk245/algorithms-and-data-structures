# Array

## Definition

- Array is fundamental data structure that is built-in in nearly every programming language.

- They are used to represent a collection of values where each value is referenced using an index or a key.

- They are also used as building blocks for other data structures. (sucs as strings in some languages)

- The fundemental qualities of arrays are same in almost every language. However, there are differences depending on the language you are using. - In languages like C, Swift or Java, arrays are homogeneous containers, which means that they can only contain the values of the same type. - In other languages such as Python or Javascript, arrays are heterogeneous structures, that means they can store any value of any type.

- Arrays are contiguous data structures. They are stored in blocks of memory that are next to each other, with no gaps. This quality allows arrays to be relatively fast when retrieving values.

## Common Operations and Their Time Complexities

  1. Access and Read Values = O(1)
        -  Elements in arrays are identified by their indexes, which are used to access and read those elements.
        - Due to being stored in contiguous blocks of same size (either the actual data in typed arrays or pointers in other), the address of each element can be calculated individually, without the need to go over other elements in the array.
        - Therefore, accessing and reading an element in an array are constant time operations, regardless of the size of the array.
   2. Search Values = O(n)
        - While arrays are really fast at accessing values, they are pretty bad at searching.
        - The defualt search operators (Python in, JavaScript includes) run linear searches under the hood and go through elements of the arrayone by one.
        - Therefore searching a value in an array is a linear time operation, taking array size steps in the worst case.
        - In the cases that the array is sorted, we can run a binary search. However, since sorting an array comes with its own cost and since linear search may operate faster for smaller sized arrays, languages stick with linear search under the hood.
   3. Insert and Deleting Values
         - Insert
            - There are three different types of insert operations.
                1. Insert = O(n)
                    - This refers to operations where a value is inserted at a user defined index.
                    - Since each of the values in the following indexes has to be moved by one, this operation takes linear time.
                    - Example: in an array of size 4, if we insert an element to index 1, the original index 1 has to be shifted to index 2, index 2 to 3, index 3 to       4
                    - Since any operation that requires going through values (each value in worst case) is linear time, inserting a value to a specific index is a linear time operation.
                2. Append / Push = O(1)
                    - This refers to operations where a value is inserted at the end of the array.
                    - Since the operation does not have to go through elements or modify them, this is a constant time operation.
                3. Extend / Concat = O(k)
                    - This refers to operations where an array is added to another.
                    - This operation effectively do consecutive append calls for each of the elements in the array to be added.
                    - If we want to add an array size of K to an array size of N, the runtime would be O(k).
            - Note: Depending on the language, the insertion operations may increase in complexity due to the resizing of the array. In Python, the arrays get dynamically resized by constant growth factors in order not to resize the array in each value insertion.
         - Delete
            - Delete operations are similar to insert operations, since when a delete operation occurs the array has to adjust the index values accordingly.
            - If we delete the first element in the array, every element in the array has to be shifted to the left.
            - Therefore delete operations have an upper bound of O(n).
            - Just like the insertion, deleting values from the very end of the array, with operators like **pop** is a constant time operation since it does not modify any other element's index in the array.


## Real-world Use

- Arrays are used one of the most common used and most fundemantal data structures in programming. Whenever a program needs to keep track of an ordered list of items, a list of songs, a list of each keystroke a user clicks, chances are it uses an array. Even in the JSON data format often uses an array to hold a list of objects.
