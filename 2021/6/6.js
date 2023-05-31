const fs = require('fs')

let data = fs.readFileSync('example.txt', 'utf8')
data = fs.readFileSync('input.txt', 'utf8')

let counts = Array(9).fill(0)
data = data.split(',').map(v=>{v=+v; counts[v]++; return v})

const cycleFish = (counts, days) => {
  for (let i=0; i<days; i++) {
    let dupes = counts.shift()
    counts[6] += dupes
    counts.push(dupes)
  }
}

const sumFish = (counts) =>{
  return counts.reduce((a,v)=>a+v,0)
}

console.log(data)
console.log(counts)
console.log('---')

cycleFish(counts, 256)
console.log(counts)
console.log(sumFish(counts))
