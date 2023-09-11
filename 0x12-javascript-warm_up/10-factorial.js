#!/usr/bin/node
import { argv } from 'node:process';
const av = argv[2];
const vl = parseInt(av);
if (!isNaN(vl)) { console.log(`${fact(Number(vl))}`); } else { console.log(1); }

function fact (number) {
  if (number === 0) { return 1; } else { return (number * fact(number - 1)); }
}
