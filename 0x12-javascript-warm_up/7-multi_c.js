#!/usr/bin/node
const arg = 'C is fun';
const times = process.argv[2];
if (times) {
  for (let i = 0; i < times; i++) {
    console.log(arg);
  }
} else if (!times) {
  console.log('Missing number of arguments');
}
