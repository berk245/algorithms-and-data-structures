# **INSERTION SORT**

This markdown analysis the insertion sort algorithm. It includes:

- The goal of the algorithm
- Inputs
- Termination Conditions
- Steps of the Algorithm
- Time and Space Complexity

## Goal

- The goal of insertion sort algorithm is to sort an unsorted sequence of numbers.

## Inputs

- The algorithm accepts an array/list as an input.

## Termination Conditions

- The algorithm terminates if the input array is empty.
- An additional checker for ensuring that the elements of array are numbers can also be added depending on the use case.

## Steps

- Insertion sort algorithm's key concept is dividing the array into two sub-arrays, sorted and unsorted.
- The initial division is after the zeroth index.

![](https://i.ibb.co/LQcmzhH/Screenshot-2021-04-08-2-Insertion-Sort-Algorithm-Explained-Full-Code-Included-Python-Algorithm-Serie.png)

- We define an indexes_to_sort variable to iterate over the 'unsorted' section of the list.
- We start a for loop in the unsorted area (in the range of indexes_to_sort).
- We look at the first element of the unsorted section, value_to_sort and 'insert' it where it belongs by comparing it with it's neighbor on its left.
- We keep on moving value_to_sort to the left until it is greater than the number on its left or the index is zero.
- We return the array after every value is moved to the sorted section of the array.

## Time and Space Complexity

### Time Complexity

- #### Best Case O(n)

  The best case scenario happens when the input array is already sorted. In that case, we do (n-1) comparisons-n being the array size- and zero swaps.

- #### Worst Case O(n^2)

  The worst case scenario happens when the input array is already sorted but in a descending order. In that case, for each unsorted element, (n-1) times, we do index times comparison and swap operations. To make it clear: - In [4,3,2,1]:
  i=1 1 comparison 1 swap
  i=2 2 comparisons 2 swaps
  i=3 3 comparisons 3 swaps

  Therefore we have an equation of:

  - 2(1) + 2(2) + 2(3) +... + 2(n-1)

  Which can be written as:

  - 2( 1 + 2 + 3 + .. + (n-3) + (n-2) + (n-1) )
    or
  - 2 ( n \* (n-1) / 2) = n^2 - n

  This equation shows that the Worst Case time complexity for Insertion Sort is quadratic, **O(n^2)**.

- #### Average Case O(n^2)

  The average case is similar to the worst case scenario. Instead of having a descending sorted list, we have two assumptions: - Half of the elements in the array will be in the right place (so no swapping operations) - Half of the values will be inserted in the middle of the 'sorted' section.

  Therefore the equation for the average case would be:

  ** (n^2)-n _ 1/2 _ 1\*2**

  Since the highest level of complexity is n^2, the time complexity of the average case is **O(n^2)**.

### Space Complexity

- The algorithm does not need any additonal memory space as the loop progresses. It only re-arranges the input array. Because of that, we can conclude that the Space Complexity of Insertion sort is O(1)
