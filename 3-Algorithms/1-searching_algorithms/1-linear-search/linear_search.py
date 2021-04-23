def simple_search(arr, target):
    if not len(arr):
        print('Empty list')
        return False
    for index in range(len(arr)):
        if arr[index] == target:
            print('Found Here', index)
            return index
    print('Not found')
    return False


'''
    Simple or linear search is an example of linear run time complexity.

    GOAL
        The goal of the algorithm is to find the target value's index in the provided array.

    INPUTS:
        The algorithm accepts two inputs; an array and a target value to be found in the array.

    TERMINATION CONDITIONS:
        The algorithm terminates/returns in three conditions:
        1) If the provided array is empty
        2) If the target value is found
        3) If end of the array is reached without finding the target value

    STEPS
        The search starts from the first element of the array. If that is equal to the target value,
        the current index is returned. If not, the algorithm moves on to the next index. This comparison
        continues until the two values match (case a) or the end of the array is reached (case b).
        When case a:
            - The index is returned and the function terminates
        When case b:
            - 'Not found' string is returned and the function terminates

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

arr = [1, 2, 3, 4, 5, 6, 7, 8]

simple_search(arr, 4)
simple_search(arr, 10)
simple_search([], 5)
