#!/usr/bin/node
// script that prints a square

const arg = process.argv[2];
const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
