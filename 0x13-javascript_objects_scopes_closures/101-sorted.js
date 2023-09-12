#!/usr/bin/node
const dictionary = require('./101-data').dict;
const arry = [];
Object.entries(dictionary).forEach((entry) => {
  arry.push(entry);
});
const obj = {};
arry.forEach((line) => {
  const key = line[1];
  const value = line[0];
  if (Object.prototype.hasOwnProperty.call(obj, `${key}`) === false) { obj[`${key}`] = [`${value}`]; } else { obj[`${key}`].push(`${value}`); }
});
console.log(obj);
