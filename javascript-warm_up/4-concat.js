#!/usr/bin/env node

/*
This script concatenates two arguments passed to it.
- If less than two arguments are passed, it prints "undefined is undefined"
- If two arguments are passed, it prints their concatenation
*/
const arg = process.argv;

console.log(arg[2] + ' is ' + arg[3]);
