function sort(arr) {
  /* Write your code here
    No need to specify return type 
    Input and output already taken care of */

  // You don't need to return anything , just sort the array in-place
  let low = 0,
    mid = 0,
    high = arr.length - 1;

  while (mid <= high) {
    if (arr[mid] === 0) {
      [arr[low], arr[mid]] = [arr[mid], arr[low]];
      mid++;
      low++;
    } else if (arr[mid] === 1) {
      mid++;
    } else {
      [arr[mid], arr[high]] = [arr[high], arr[mid]];
      high--;
    }
  }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");

let input_stdin = "";
let input_stdin_array = "";
let input_currentline = 0;

process.stdin.on("data", function (data) {
  input_stdin += data;
});

process.stdin.on("end", function () {
  input_stdin_array = input_stdin.split("\n");
  main();
});

function readLine() {
  return input_stdin_array[input_currentline++];
}

function main() {
  let t = parseInt(readLine());

  while (t-- > 0) {
    let n = parseInt(readLine());
    const arr = readLine().replace(/\s+$/g, "").split(" ");

    let array = [];

    for (let i = 0; i < n; i++) {
      array.push(Number(arr[i]));
    }

    let res = sort(array);
    console.log(array.join(" "));
  }
}
