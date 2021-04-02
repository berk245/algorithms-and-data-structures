function checkDuplicates(arr) {
  let steps = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      steps += 1;
      console.log("step:", steps);
      if (i != j) {
        if (arr[i] == arr[j]) {
          //   console.log("Found Duplicates", arr[i], arr[j]);
        }
      }
    }
  }
}

let example = [1, 2, 3, 4, 4, 3, 2, 1, 6, 5, 4, 2, 3, 1];

checkDuplicates(example);
