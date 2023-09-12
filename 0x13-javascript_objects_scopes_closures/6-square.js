#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
