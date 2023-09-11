#!/usr/bin/node
const a = process.argv[2];
const vl = parseInt(a);
if (!isNaN(vl)) {
  for (let index = 0; index < Number(vl); index++) {
    console.log('C is fun');
  }
} else { console.log('Missing number of occurrences'); }
