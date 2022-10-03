#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  const value = process.argv.sort();
  console.log(value[len - 2]);
}
