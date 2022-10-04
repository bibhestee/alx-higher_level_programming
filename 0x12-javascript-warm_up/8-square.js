#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    let sq = 'X';
    for (let j = 1; j < size; j++) {
      sq += 'X';
    }
    console.log(sq);
  }
} else if (!size) {
  console.log('Missing size');
}
