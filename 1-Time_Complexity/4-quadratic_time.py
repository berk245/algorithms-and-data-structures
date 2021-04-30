def quadratic_time(arr):
    counter = 0
    for val in arr:
        for val in arr:
            counter += 1
    print(counter)


arr = [1, 2, 3, 4, 5]

quadratic_time(arr)

'''
Quadratic Time Complexity refers to the cases in which the execution time of an algorithm is proportional to the squared size of the input data set (similar to linear, but squared). 
This time complexity usually occurs when there are multiple for-loops nested. 

The example above is an example for O(n^2) time complexity (although probably the function itself does not make sense :)). 
The function iterates through each element of the array. In each iteration, another for loop gets executed that goes through every other item in the array. 
This double iteration leads to the quadratic runtime.  
'''
