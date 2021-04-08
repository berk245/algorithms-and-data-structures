def insertion_sort(arr):
    if(len(arr) == 0):
        return arr

    indexes_to_sort = range(1, len(arr))
    for index in indexes_to_sort:
        value_to_sort = arr[index]
        while value_to_sort < arr[index-1] and index > 0:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
    return arr


'''
    GOAL
        The goal of insertion sort algorithm is to sort an unsorted sequence of numbers.

    INPUTS:
        The algorithm accepts an array.

    TERMINATION CONDITIONS:
        The algorithm terminates if the input array is empty. 
        An additional checker for ensuring that the elements of array are numbers can also be added depending on the use case.

    STEPS
        Insertion sort 

    TIME COMPLEXITY
        1) Best Case:
            If the target value is located in the very beginning of the array, the search takes only 
            one step to complete. Therefore it would be constant time. (O(1))

        2)Worst Case:
            The number of steps/calculations increases if the target value is located in the end of the
            array or if the array does not include the target value. In these cases, in order to terminate,
            the algorithm has to make as many operations as the size of the array. 
            Therefore, the worst case time complexity is dependant on the array size and has a linear time complexity,
            O(n)

        3)Average Case:
            In the average case, the target value is located close to the middle of the array. Depending on the array size and
            if the array is sorted, linear search can be an acceptable/rational algorithm choice.  


'''


unsorted = [14, 5, 3, 33, 21, 13, 45]

print(insertion_sort(unsorted))
