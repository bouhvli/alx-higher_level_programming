#!/usr/bin/node
import { argv } from 'node:process';
if (argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
