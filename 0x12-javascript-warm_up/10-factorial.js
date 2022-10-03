#!/usr/bin/node
function factorial (x) {
  if (!x) {
    console.log(1);
  } else {
    let result = 1;
    while (x !== 1) {
      result *= x;
      x--;
    }
    console.log(result);
  }
}
const num = parseInt(process.argv[2]);
factorial(num);
