function indexTimesTwo(arr) {
  for (let i = 1; i < arr.length; i *= 2) {
    console.log(arr[i]);
  }
}

indexTimesTwo([1, 2, 3, 4, 5, 6, 7, 8, 9, , 10, 11, 12, 13, 14, 15, 16]);

/*
    Logarithmic Time Complexity refers to an algorithm that runs in proportionally to the logarithm of the input size.
    Note: This simple example is written in JS for using it's for loop incrementation syntax.

    The example above takes an array as an argument and iterates over it, starting from the first index.
    In each iteration, the value of i (index) is doubled, until it becomes greater than the array size.

    The time complexity is not constant, since it changes based on the array size. The function needs to take one additional 
    step as the array size doubles. Therefore this function has a logarithmic time complexity O(log n)



    */
