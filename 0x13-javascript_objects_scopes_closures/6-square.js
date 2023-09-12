#!/usr/bin/node
const NewSquare = require('./5-square');

class Square extends NewSquare {
  charPrint (c) {
    for (let index = 0; index < this.height; index++) {
      if (c === undefined) { console.log('X'.repeat(this.width)); } else { console.log('C'.repeat(this.width)); }
    }
  }
}
module.exports = Square;
