#!/usr/bin/node
import { argv } from 'node:process';
const a = argv[2];
const b = argv[3];
const vl = parseInt(a);
const vl1 = parseInt(b);
if (!isNaN(vl) && !isNaN(vl1)) {
  console.log(Number(vl) + Number(vl1));
} else { console.log(NaN); }
