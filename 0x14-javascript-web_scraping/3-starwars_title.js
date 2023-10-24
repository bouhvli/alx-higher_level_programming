#!/usr/bin/node
const req = require('request');
const apiStarWar = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);
req(apiStarWar, (_error, _response, body) => {
  const res = JSON.parse(body);
  console.log(res.title);
});
