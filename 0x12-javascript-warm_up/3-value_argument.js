#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  process.argv.forEach((val, idx) => {
    if (idx >= 2) {
      console.log(`${val}`);
    }
  });
}
