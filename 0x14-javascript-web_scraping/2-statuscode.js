#!/usr/bin/node
const req = require('request');
req(process.argv[2], (_error, response) => {
  console.log('code:', response.statusCode);
});
