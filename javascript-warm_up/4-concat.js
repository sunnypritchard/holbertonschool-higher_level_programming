#!/usr/bin/node

/*
This script concatenates two arguments passed to it.
- If less than two arguments are passed, it prints "undefined is undefined"
- If two arguments are passed, it prints their concatenation
*/
const args = process.argv;
const arg1 = args[2];
const arg2 = args[3];

if (arg1 === undefined || arg2 === undefined) {
  console.log('undefined ' + 'is ' + 'undefined');
} else {
  console.log(arg1 + ' is ' + arg2);
}
