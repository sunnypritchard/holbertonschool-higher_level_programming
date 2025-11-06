#!/usr/bin/node

/*
This script prints a square with the character 'X'.
- If no argument is passed, it prints "Missing size"
*/
const args = process.argv;
const size = parseInt(args[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
