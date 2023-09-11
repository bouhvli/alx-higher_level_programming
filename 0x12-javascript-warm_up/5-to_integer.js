#!/usr/bin/node
const a = process.argv[2];
const vl = parseInt(a);
if (!isNaN(vl)) {
  console.log(`My number: ${Number(vl)}`);
} else { console.log('Not a number'); }
