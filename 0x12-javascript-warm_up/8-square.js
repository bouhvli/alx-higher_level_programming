#!/usr/bin/node
const a = process.argv[2];
const vl = parseInt(a);
if (!isNaN(vl)) {
  for (let index = 0; index < Number(vl); index++) {
    let output = '';
    for (let jdx = 0; jdx < Number(vl); jdx++) {
      output += 'X';
    }
    console.log(output);
  }
} else { console.log('Missing number of occurrences'); }
