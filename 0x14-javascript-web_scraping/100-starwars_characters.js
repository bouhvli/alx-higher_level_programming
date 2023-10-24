#!/usr/bin/node
const req = require('request');
const apiStarWar = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
req(apiStarWar, (_error, _response, body) => {
  const res = JSON.parse(body).characters;
  let idx = 0;
  while (idx < res.length) {
    req(res[idx], (_charError, _charResponse, charBody) => {
      console.log(JSON.parse(charBody).name);
    });
    idx += 1;
  }
});
