#!/usr/bin/node
// script that prints x times “C is fun”

const arg = process.argv[2];
const intValue = parseInt(arg);

if (!isNaN(intValue)) {
  for (let i = 0; i < intValue; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
