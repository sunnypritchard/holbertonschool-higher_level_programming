#!/usr/bin/node

/*
This script prints three lines useing a loop:
- C is fun
- Python is cool
- JavaScript is amazing
*/

const languages = ['C', 'Python', 'JavaScript'];
const qualities = ['fun', 'cool', 'amazing'];

for (let i = 0; i < languages.length; i++) {
    console.log(languages[i] + ' is ' + qualities[i]);
}
