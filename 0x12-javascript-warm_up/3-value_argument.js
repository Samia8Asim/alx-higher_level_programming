#!/usr/bin/node
// prints the first argument passed to the script

const numArg = process.argv.length - 2;
if (numArg === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
