#!/usr/bin/node

/*
This script prints x times "C is fun", where x is the first argument passed to it.
- If the argument is not a number, it prints "Missing number of occurrences"
*/
const args = process.argv;
const x = parseInt(args[2], 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
