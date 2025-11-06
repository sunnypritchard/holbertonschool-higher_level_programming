#! /usr/bin/env node

/*
This script prints the first argument passed to it.
- If no arguments are passed, it prints "No argument"
- If an argument is passed, it prints that argument
*/

const args = process.argv;
const arg1 = args[2];

if (arg1 === undefined) { console.log('No argument'); } else {
  console.log(arg1);
}
