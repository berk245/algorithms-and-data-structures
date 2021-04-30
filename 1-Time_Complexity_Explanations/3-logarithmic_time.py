def arraySlicer(arr):
    print('Array length:', len(arr))
    steps = 0
    while (len(arr) > 1):
        mid = len(arr) // 2
        arr = arr[:mid]
        steps += 1
    print('Step count:', steps)
    print('-------')


arraySlicer([1, 2, 3, 4])

arraySlicer([1, 2, 3, 4, 5, 6, 7, 8])

arraySlicer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arraySlicer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

'''
Logarithmic Time Complexity refers to the cases in which the execution time of an algorithm is proportional to the logarithm of the input size.

The example above takes an array as an input and halves the array until the remaining array size is 1.

The time complexity is not constant, since it changes based on the array size. The function needs to take one additional step as the array size doubles. Therefore this function has a logarithmic time complexity O(log n)

The justification for logarithmic time is as follows:

- The while loop inside the function runs until the array size is equal to 1. The number of times the while loop executes is equal to the
number of times we have to divide the array size to two. If we have an array of size n as input, the sizes will be as follows after each iteration:
      Iter. #1: n/2
      Iter. #2: n/2/2
      Iter. #3: n/2/2/2
      .
      .
      .
      Iter. #k: n/2^k or 1

- K is the number of divisions we do in order to reach one. 
- Since n/2^k is the last level and should be equal to one,
	- n equals 2^k. 
	- Because of this, k = log2n
- Therefore in order for k to increase by one, n should be doubled.


'''
