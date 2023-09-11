#!/usr/bin/node
import { argv } from 'node:process';
if (argv.length <= 2) {
  console.log('No argument');
} else {
  argv.forEach((val, idx) => {
    if (idx >= 2) {
      console.log(`${val}`);
    }
  });
}
