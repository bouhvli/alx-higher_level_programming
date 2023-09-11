#!/usr/bin/node
import { argv } from 'node:process';
const a = argv[2];
const vl = parseInt(a);
if (!isNaN(vl)) {
  console.log(`My number: ${Number(vl)}`);
} else { console.log('Not a number'); }
