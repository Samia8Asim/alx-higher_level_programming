#!/usr/bin/node
// class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return 'Rectangle {}';
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}
module.exports = Rectangle;
