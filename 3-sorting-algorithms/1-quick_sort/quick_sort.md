# **Quick Sort**

This markdown analysis the quicksort algorithm. It includes:

- The goal of the algorithm
- Inputs
- Termination Conditions
- Steps of the Algorithm
- Time and Space Complexity
- Usecases

- In this folder, two different implementations of quicksort can be found. This analysis is on the implementation with partition (2-quick_sort_partition) since it is a more sophisticated solution with no additional space requirements (no sublists in each iteration, smaller space complexity)

## Goal

- The goal of the algorithm is to sort an unsorted sequence of numbers.

## Inputs

- The algorithm takes three inputs:

  - Array to be sorted
  - The start index
  - The end index

- Start and end indices refer to the pointers that initially point to the start and end of the array. In later iterations, they allow us to do the sorting in subarrays. The purpose and use of them will become more clear in the 'Steps' section.

## Termination Conditions

- My quicksort implementation does not have a clearly defined termination condition. The checks for length of the array or ensuring the input left and right index values make sense (left is smaller than right) are omitted since the partition function only operates when those values are valid.
- Having said that, the algorithm raises an error and terminates if the user fails to input 3 parameters; 1 array, and 2 integers

## Steps

- This quicksort implementation relies heavily on another function called partition. In this section, both partition and quick_sort functions are going to be analysed individually.
- ### Partition

  - The goal of this function is to select a pivot value from the array and arrange a rough order based on this value. The values that are smaller than the pivot will be on the left side of the pivot's index and the ones that are greater will be on the right. At the end, the index of the pivot will be returned. Here are the steps:

  1. **Find a pivot element in the array and save its initial index in a variable.**
     - In this implementation it is the first value of the array. This can be changed for optimizitaion purposes(choosing a random pivot or choosing the middle element are some options)
  2. **Start a while loop that goes on until left pointer is equal or greater than right pointer. Within this while loop:**

     - While the value of array[left_pointer] is less than the pivot value, move the left pointer to the right by incrementing it. Continue until array[left_pointer] is greater than or equal to the pivot value.
     - While the array[right_pointer] is greater than the pivot value, move the right pointer to the left by decrementing it. Continue until array[right_pointer] is less than or equal to the pivot value.
     - If right_pointer is greater than the left_pointer, swap the values they are pointing to.

  3. **After the while loop finishes, swap the pivot value with the array[right_pointer]**
     - This operation inserts the pivot in its sorted position. The original at that point is partially sorted. The values on the left side of the pivot are smaller than the pivot and vice versa.

- ### Quicksort
  1. Run the partition function on the input array and find the index of the pivot value.
  2. Call quick_sort on the initial array with start_index 0 and end_index pivot_index-1. (values in this section are smaller than the pivot value)
  3. Call quick_sort on the initial array with start_index pivot_index + 1 and end_index last elemetn of the array. (values in this section are bigger than the pivot value)
  4. Steps 2 and 3 recursively call the same function until a subarray has zero or one elements (or in other words when start index is equal to end index)
  5. Finally, return the sorted array.

## Time and Space Complexity

### Time Complexity

- #### Best Case O(n)

- #### Worst Case O(n^2)

- #### Average Case O

### Space Complexity

- The algorithm does not need any additonal memory space as the loop progresses. It only re-arranges the input array. Because of that, we can conclude that the Space Complexity of Insertion sort is O(1)
