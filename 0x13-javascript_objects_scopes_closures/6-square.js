#!/usr/bin/node
const NewSquare = require('./5-square');

class Square extends NewSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let index = 0; index < this.height; index++) {
        let line = '';
        for (let jdx = 0; jdx < this.width; jdx++) {
          line += 'C';
        }
        console.log(line);
      }
    }
  }
}
module.exports = Square;
