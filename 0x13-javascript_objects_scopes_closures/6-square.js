#!/usr/bin/node
const NewSquare = require('./5-square');

class Square extends NewSquare {
  charPrint (c) {
    for (let index = 0; index < this.height; index++) {
      let line = '';
      for (let jdx = 0; jdx < this.width; jdx++) {
        if (c === undefined) { line += 'X'; } else { line += c; }
      }
      console.log(line);
    }
  }
}
module.exports = Square;
