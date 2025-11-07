#!/usr/bin/node

/*
This script script searches for the biggest integer in the list of arguments passed to it.
- If no arguments are passed, it prints 0
- If the number of arguments passed is 1, it prints 0
- If the number of arguments passed is 2 or more, it prints the second biggest integer
*/

const args = process.argv.slice(2);
const numbers = args.map((arg) => parseInt(arg, 10));

if (numbers.length < 2) {
  console.log(0);
} else {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
