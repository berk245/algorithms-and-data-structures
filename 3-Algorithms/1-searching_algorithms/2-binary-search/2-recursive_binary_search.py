def recursive_binary_search(list, target):
    '''
    Returns true if target is found, false if not found or the list is empty.
    '''
    if(len(list) == 0):
        print('Target not found')
        return False

    midpoint = (len(list))//2

    if list[midpoint] == target:
        print('Target found')
        return True
    else:
        if list[midpoint] < target:
            sliced_list = list[midpoint+1:]
            return recursive_binary_search(sliced_list, target)
        else:
            sliced_list = list[0:midpoint]
            return recursive_binary_search(sliced_list, target)


'''

    GOAL
        The goal of the algorithm is to find the target value's index in the provided array.
        Important: Binary search can return successful results when applied to sorted arrays only.

    INPUTS:
        The algorithm accepts two inputs; an array and a target value to be found in the array.

    TERMINATION CONDITIONS:
        Since this is a recursive function, in each run, the function returns a value:
        1) If the provided array is empty, False is returned
        2) If the target value is equal to the array[midpoint], True is returned.
        3) Depending on the comparison of array[midpoint] and target, the function returns a function call to itself, with sliced arrays.

    STEPS
        The first step is to check if the array has any elements. If it does not, the algorithm returns False.
        Next, the midpoint of the provided array is calculated.
        If array[midpoint] is equal to target value the algorithm returns True
        If array[midpoint] is smaller than target:
            We define a new subarray of the original array, by slicing it from the midpoint+1 index to the last element
            The function calls itself with the sliced array and target value
        If array[midpoint] is greater than target:
            We define a new subarray of the original array, by slicing it from the first element to the midpoint-1 index
            The function calls itself with the sliced array and target value       

    TIME COMPLEXITY: O(log n)
        The time complexity of the recursive binary search is identical to the iterative one. (See 1-binary_search.py). The main difference is the space complexity.

    SPACE COMPLEXITY: O(log n)
        This algorithm implementation relies on calling the same function again with different inputs. This is especially favored in functional languages since changing the values that are used in a function is considered a bad practice. On each function call of the recursive binary search, we create a sublist that is half the size of the original one, to pass to the next call. 
        For an original array of size N, the next sub-array will be N/2, the next is N/4, n/8, and so on. That is why this execution has logarithmic time complexity.
        **IMPORTANT**
        The space complexity of recursive implementation can vary depending on the language it is written. Some languages have features to make recursion more space-efficient, such as Tail call optimization in Swift. The above explanation applies to Python.
    
    USE CASES
    Although recursive and iterative implementations of the same search algorithm have the same run time complexity, when applied in Python or a language that does not have a tail call 
    optimization like features, using the iterative implementation is the more rational choice because of its constant space complexity (when compared to logarithmic)
    

    '''


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
recursive_binary_search(numbers, 12)
