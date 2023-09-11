#!/usr/bin/node
if (process.argv.length <= 3) { console.log('0'); } else {
  const array = [];
  process.argv.flatMap(function (n) {
    const vn = parseInt(n);
    if (!isNaN(vn)) {
      array.push(vn);
      return vn;
    }
    return 0;
  });
  array.sort((x, y) => x - y);
  console.log(array[array.length - 2]);
}
