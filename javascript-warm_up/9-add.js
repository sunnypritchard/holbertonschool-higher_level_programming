#!/usr/bin/node

/*
This script prints an addition of two numbers passed as arguments.
- If two numbers are passed, it prints their sum.
- If less than two numbers are passed, it prints "NaN".
*/

function add (a, b) {
  return a + b;
}

const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);

console.log(add(num1, num2));
