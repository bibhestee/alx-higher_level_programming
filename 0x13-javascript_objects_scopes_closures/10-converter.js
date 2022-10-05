#!/usr/bin/node
exports.converter = function (base) {
  const b = base;
  function cvt (base) {
    return base.toString(b);
  }
  return cvt;
};
