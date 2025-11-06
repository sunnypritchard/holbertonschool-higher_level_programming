#!/usr/bin/env node

/*
This script prints a message depending on the number of arguments passed:
- If no arguments are passed, it prints "No argument"
- If one argument is passed, it prints "Argument found"
- If two or more arguments are passed, it prints "Arguments found"
*/
const argCount = process.argv.length - 2;

if (argCount === 3) {
    console.log('No argument');
} else if (argCount > 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
