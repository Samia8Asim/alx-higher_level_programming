#!/usr/bin/node
// function that prints the number of arguments

let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
