#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

if (process.argv.length < 3) {
  console.log(0);
} else if (process.argv.length < 4) {
  console.log(0);
} else {
  let bigNum = parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > bigNum) {
      bigNum = parseInt(process.argv[i]);
    }
  }
  console.log(bigNum);
}
