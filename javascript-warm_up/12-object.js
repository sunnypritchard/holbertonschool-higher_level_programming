#!/usr/bin/node

/*
This script updates the value of an object's property
and prints the object before and after the update.
*/
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);
myObject.value = 89;
console.log(myObject);
