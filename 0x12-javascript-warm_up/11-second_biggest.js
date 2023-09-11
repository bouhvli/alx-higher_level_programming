#!/usr/bin/node
import { argv } from 'node:process';
if (argv.length <= 3) { console.log(0); } else {
  const array = [];
  argv.flatMap(function (n) {
    const vn = parseInt(n);
    if (!isNaN(vn)) {
      array.push(Number(vn));
      return Number(vn);
    }
    return 0;
  });
  array.sort();
  console.log(array[array.length - 2]);
}
