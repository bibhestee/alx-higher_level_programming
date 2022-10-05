#!/usr/bin/node
const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let sq = c;
      for (let j = 1; j < this.height; j++) {
        sq += c;
      }
      console.log(sq);
    }
  }
};
