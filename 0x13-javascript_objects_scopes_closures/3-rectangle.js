#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      let line = '';
      for (let jdx = 0; jdx < this.width; jdx++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}
module.exports = Rectangle;
