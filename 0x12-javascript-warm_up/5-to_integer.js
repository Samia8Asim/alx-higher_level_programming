#!/usr/bin/node
//  prints My number: <first argument converted in integer>

const arg1 = process.argv[2];
if (!isNaN(parseInt(arg1))) {
	console.log(`My number: ${parseInt(arg1)}`);
} else {
	console.log('Not a number');
}
