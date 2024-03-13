#!/usr/bin/node
// script that imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.

const data = require('./101-data');
const newDict = {};

for (const id in data.dict) {
  const count = data.dict[id];

  if (count in newDict) {
    newDict[count].push(id);
  } else {
    newDict[count] = [id];
  }
}

console.log(newDict);
