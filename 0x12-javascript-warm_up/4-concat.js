#!/usr/bin/node
// prints the first two arguments passed to the script

const [,, arg1, arg2] = process.argv;
console.log(`${arg1 || 'undefined'} is ${arg2 || 'undefined'}`);
