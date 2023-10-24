#!/usr/bin/node
const req = require('request');
const apiStarWar = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

const retrive = (array, idx) => {
  if (idx === array.length) return;
  req(array[idx], (error, response, body) => {
    if (error) console.log(error);
    console.log(JSON.parse(body).name);
    retrive(array, idx + 1);
  });
};

req(apiStarWar, (error, _response, body) => {
  if (error) console.log(error);
  const res = JSON.parse(body).characters;
  retrive(res, 0);
});
