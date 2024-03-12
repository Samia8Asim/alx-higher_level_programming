#!/usr/bin/node
// script that computes and prints a factorial

function factorial (a) {
  if (isNaN(a) || a <= 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
