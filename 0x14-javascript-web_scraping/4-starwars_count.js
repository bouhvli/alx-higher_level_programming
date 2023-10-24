#!/usr/bin/node
const req = require('request');
const apiStarWar = process.argv[2];
let count = 0;
req(apiStarWar, (_error, _request, body) => {
  const response = JSON.parse(body).results;
  let idx = 0;
  while (idx < response.length) {
    const chars = response[idx].characters;
    let jdx = 0;
    while (jdx < chars.length) {
      const char = chars[jdx];
      const charId = char.split('/')[5];
      count += (charId === '18') ? 1 : 0;
      jdx += 1;
    }
    idx += 1;
  }
  console.log(count);
});
