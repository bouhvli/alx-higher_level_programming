#!/usr/bin/node
if (process.argv.length <= 3) { console.log(0); } else {
  const array = process.argv.sort();
  console.log(array[array.length - 2]);
}
