#!/usr/bin/node
const list = require('./100-data').list;
const resMap = list.map((x, idx) => x * idx);
console.log(list);
console.log(resMap);
