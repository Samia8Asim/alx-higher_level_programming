#!/usr/bin/node
const fs = require('fs');

const f1Path = process.argv[2];
const f2Path = process.argv[3];
const destPath = process.argv[4];

fs.readFile(f1Path, 'utf-8', (err, data1) => {
	if (err) {
		process.exit(1);
	}
	fs.readFile(f2Path, 'utf-8', (err, data2) => {
		if (err) {
			process.exit(1);
		}

		const concatdData = `${data1}${data2}`;
		fs.writeFile(destPath, concatdData, err => {
			if (err) {
				process.exit(1);
			}
		});
	});
});
