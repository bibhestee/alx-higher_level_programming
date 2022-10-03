#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    let sq = 'x';
    for (let j = 1; j < size; j++) {
      sq += 'x';
    }
    console.log(sq);
  }
} else if (!size) {
  console.log('Missing size');
}
