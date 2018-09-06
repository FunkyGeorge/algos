

const map = {};

for (let a = 1; a < 1000; a += 1) {
  for (let b = 1; b < 1000; b += 1) {
    map[Math.pow(a, 3) + Math.pow(b, 3)] = [a, b];
  }
}

let count = 0;

for (let a = 1; a < 1000; a += 1) {
  for (let b = 1; b < 1000; b += 1) {
    const key = Math.pow(a, 3) + Math.pow(b, 3);
    console.log(`a = ${a}, b = ${b}, c = ${map[key][0]}, d = ${map[key][1]}`);
    count++;
    if (map[key][0] !== map[key][1]) {
      console.log(`a = ${a}, b = ${b}, c = ${map[key][1]}, d = ${map[key][0]}`);
      count++;
    }
  }
}

console.log(Object.keys(map).length);
console.log(count);