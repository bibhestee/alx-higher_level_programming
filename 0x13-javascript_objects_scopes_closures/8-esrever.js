#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const len = list.length;
  for (let i = 0; i < len; i++) {
    newList[i] = list.pop();
  }
  return newList;
};
