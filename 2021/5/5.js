const fs = require('fs')

let data = fs.readFileSync('example.txt', 'utf8')
data = fs.readFileSync('input.txt', 'utf8')

// console.log(data)
let max = 0
let lines = data.split('\n').map(line=>{
  let [a,b] = line.split(' -> ')
  a = a.split(',')
  a[0] = +a[0]
  a[1] = +a[1]
  b = b.split(',')
  b[0] = +b[0]
  b[1] = +b[1]

  max = Math.max(max, ...a, ...b)
  return [a,b]
})
max++

let map = Array(max).fill([]).map(v=>Array(max).fill(0))

const mapLine = (map, line, allowDiag=false) => {
  let [start, end] = line
  if (!allowDiag && !(start[0] === end[0] || start[1] === end[1])) return
  
  let x, y
  for (let i=0; i<=Math.abs(start[0]-end[0]); i++) {
    x = start[0] < end[0] ? start[0] + i : start[0] - i
    
    for (let j=0; j<=Math.abs(start[1]-end[1]); j++) {
      if (i !== j && (start[0] !== end[0] && start[1] !== end[1])) continue
      y = start[1] < end[1] ? start[1] + j : start[1] - j
  
      map[y][x] += 1
    }
  }
}

const sumMap = map => {
  return map.reduce((aLine, line)=>{
    return aLine + line.reduce((a,v)=>{
      return a + (v >= 2 ? 1 : 0)
    },0)
  },0)
}

const printMap = map => {
  map.forEach(line=>console.log(line.join('').replaceAll('0','.')))
}

// lines.forEach(line=>mapLine(map, line))
lines.forEach(line=>mapLine(map, line, true))

printMap(map)
console.log('---')
console.log(sumMap(map))
