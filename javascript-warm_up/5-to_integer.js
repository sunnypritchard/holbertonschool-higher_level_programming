#!/usr/bin/node

/*
This script prints a message with the first argument passed converted to an integer.
- If the argument cannot be converted to an integer, it prints "Not a number"
*/

const args = process.argv;
const arg1 = args[2];
const intArg = parseInt(arg1, 10); // Convert to integer with base 10

if (isNaN(intArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + intArg);
}
