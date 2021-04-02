def binary_search(list, target):
    # Set initial values for start and end indexes/position
    start_index = 0
    end_index = len(list) - 1  # Constant time operation in python

    while start_index <= end_index:
        midpoint = (start_index + end_index)//2  # Constant time

        if list[midpoint] == target:  # Constant time
            return midpoint
        elif list[midpoint] < target:   # Constant time
            start_index = midpoint + 1
        else:
            end_index = midpoint - 1

    return False

    '''
    GOAL
        The goal of the algorithm is to find the target value's index in the provided array.
        Important: Binary search can return successful results when applied to sorted arrays only.

    INPUTS:
        The algorithm accepts two inputs; an array and a target value to be found in the array.

    TERMINATION CONDITIONS:
        The algorithm terminates/returns in three conditions:
        1) If the provided array is empty
        2) If the target value is found
        3) If the start_index and end_index are equal(array with a single element) and the target is not found

    STEPS
        The algorithm starts by setting the start and end indexes.
        In the initial run these are equal to the first and last element of the list.
        While these two values are not equal:
            1) We define a midpoint variable is defined to access the value in the middle of the array
            2) We check if the array[midpoint] is equal to the target value. 
            3) If they are equal, we RETURN the index (midpoint)
            4) If they are not equal and
                a. target value is smaller than the array[midpoint]
                    - we eliminate all the values that are after the midpoint index by setting the new end_index to midpoint-1
                    - Since the array is sorted, we know that if midpoint is greater than the target, every value that is located after the 
                    midpoint index will also be greater than the target.
                b. target value is greater than the array[midpoint]
                    - we eliminate all the values that are before the midpoint index by setting the new start_index to midpoint+1
                    - Since the array is sorted, we know that if midpoint is smaller than the target, every value that is located before the 
                    midpoint index will also be smaller than the target.
        If nothing is returned at the end of the while loop, that means the target value is not found in the array and the function returns False
        

    TIME COMPLEXITY: O(log n)
        1) Best Case:
            If the target value is located exactly in the midpoint index, the search would return a value almost instantly, regardless of the array size. 
            Therefore it would be constant time. (O(1))

        2)Worst Case:
            In general, for a given array size of n, the number of tries binary search takes to find the worst case scenario is log2 of n plus 1. O(log n)

        - In each iteration of the while loop, the size of the array is halved. That is why when the array size(n) is doubled, the algorithm needs only one more step
        to complete the search. 
        -Below you can see the required steps for binary search to complete with different array sizes.
            Target: Last element of arrray
            [1...16] => midpoints = 8 => 12 => 14 => 15 => 16 (5 tries)
            [1...32] => midpoints = 16 => 24 => 28 => 30 => 31 => 32 (6 tries)
            [1...64] => midpoints = 32 => 48 => 56 => 60 => 62 => 63 => 64 (7 tries)

    SPACE COMPLEXITY: O(1)
        This algorithm implementation relies heavily on two variables, start_index and end_index, which are assigned new values as the algorithm proceeds.
        When we eliminate one part of the array, we do not create a new sublist. Instead we just change the indexes of the start and end. 
        Since there is no need for storing additional data during the execution of the algorithm, the space complexity is constant and independent from the 
        array size.
        Space complexity will be a key factor when comparing iterative(this example) and recursive implementations of binary search. 
    
    USE CASES
    Logartihmic runtime is preferred to linear runtime, therefore binary search is an efficient searching algortihm. However if the array is not sorted,
    binary search does not return corretct results. Depending on the case (sizeof array, position of the target), using another search algorithm, such as linear
    search, may be more time efficient than sorting the array and executing the search afterwards.
    

    '''
