function indexTimesTwo(arr) {
  for (let i = 1; i < arr.length; i *= 2) {
    console.log(arr[i]);
  }
}

indexTimesTwo([1, 2, 3, 4, 5, 6, 7, 8, 9, , 10, 11, 12, 13, 14, 15, 16]);

/*
    Logarithmic Time Complexity refers to an algorithm that runs in proportionally to the logarithm of the input size.
    Note: This simple example is written in JS for using it's for loop incrementation syntax

    */
