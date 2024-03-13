#!/usr/bin/node
// script to imports an array and computes a new array.

const data = require('./100-data');
const initList = data.list;
const newList = initList.map((val, idx) => val * idx);

console.log(initList);
console.log(newList);
