#!/usr/bin/node
const List = require('./100-data').list;
const mapping = List.map((x, index) => x * index);
console.log(List);
console.log(mapping);
