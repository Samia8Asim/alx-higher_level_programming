#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

if (process.argv.length < 3) {
  console.log(0);
} else if (process.argv.length < 4) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number);
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
