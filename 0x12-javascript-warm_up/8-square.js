#!/usr/bin/node
import { argv } from 'node:process';
const a = argv[2];
const vl = parseInt(a);
if (!isNaN(vl)) {
  for (let index = 0; index < Number(vl); index++) {
    let output = '';
    for (let jdx = 0; jdx < Number(vl); jdx++) {
      output += '#';
    }
    console.log(output);
  }
} else { console.log('Missing number of occurrences'); }