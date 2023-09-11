#!/usr/bin/node
const av = process.argv[2];
const vl = parseInt(av);
if (!isNaN(vl)) { console.log(`${fact(Number(vl))}`); } else { console.log(1); }

function fact (number) {
  if (number === 0) { return 1; } else { return (number * fact(number - 1)); }
}
