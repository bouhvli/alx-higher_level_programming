#!/usr/bin/node
import { argv } from 'node:process';
const a = argv[2];
const vl = parseInt(a);
if (!isNaN(vl)) {
  for (let index = 0; index < Number(vl); index++) {
    console.log('C is fun');
  }
} else { console.log('Missing number of occurrences'); }
