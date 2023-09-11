#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
const vl = parseInt(a);
const vl1 = parseInt(b);
if (!isNaN(vl) && !isNaN(vl1)) {
  console.log(Number(vl) + Number(vl1));
} else { console.log(NaN); }
