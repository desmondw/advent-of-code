const fs = require('fs')

let data = fs.readFileSync('./input.txt', 'utf8').split('\n').map(v=>+v)

// part 1
let increases = 0
for (let i=1; i<data.length; i++) {
  if (data[i] > data[i-1]) increases++
}
console.log(increases)

// part 2
increases = 0
// window value
let wv = [data[0] + data[1], data[1]]
console.log(data[0])
console.log(wv)

for (let i=2; i<data.length-2; i++) {
  // add to indexes
  wv[wv.length-2] += data[i]
  wv[wv.length-1] += data[i]
  wv.push(data[i])

  // compare 3rd to last val to 4th to last
  if (wv[wv.length-4] < wv[wv.length-3]) increases++
}

wv[wv.length-2] += data[data.length-2]
wv[wv.length-1] += data[data.length-2] + data[data.length-1]
if (wv[wv.length-3] < wv[wv.length-2]) increases++
if (wv[wv.length-2] < wv[wv.length-1]) increases++

console.log(wv)

console.log(increases)