#!/usr/bin/node

/*
This script computes and prints a factorial recursively.
- The first argument is the integer to compute the factorial of.
- Factorial of NaN is 1.
- Uses recursion to calculate the result.
*/

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2], 10);
console.log(factorial(num));
