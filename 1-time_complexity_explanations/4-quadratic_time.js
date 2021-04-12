function checkDuplicates(arr) {
  let steps = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      steps += 1;
      console.log("step:", steps);
      if (i != j) {
        if (arr[i] == arr[j]) {
          console.log("Found Duplicates", arr[i], arr[j]);
        }
      }
    }
  }
}

let example = [1, 2, 3, 4, 4, 3, 2, 1, 6, 5, 4, 2, 3, 1]; // array size is 14. The function takes 14*14 = 196 steps

checkDuplicates(example);

/*
    Quadratic Time Complexity represents an algorithm whose performance is directly proportional to the squared size of the input data set (similar to linear, but squared). 
    Within programs, this time complexity occurs whenever we nest over multiple iterations within the data sets.

    The example above is an example for O(n^2) time complexity (although probably the function itself does not make sense :)). 
    For each element in the array, the function starts another loop that goes through every other element in the array and thus create the quadratic runtime. 

*/
