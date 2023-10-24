#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const apiStarWar = process.argv[2];

req(apiStarWar, (_error, _request, body) => {
  fs.writeFile(process.argv[3], body, 'utf8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
