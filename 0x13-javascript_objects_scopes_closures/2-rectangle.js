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
}
module.exports = Rectangle;
