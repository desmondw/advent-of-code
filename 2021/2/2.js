const fs = require('fs')

// let data = fs.readFileSync('example.txt', 'utf8').split('\n')
let data = fs.readFileSync('input.txt', 'utf8').split('\n')
// console.log(data)

let x = 0, y = 0, aim = 0
data.forEach(v=>{
  let [cmd, delta] = v.split(' ')
  delta = +delta
  switch (cmd) {
    case 'forward':
      x += delta
      y += aim * delta
      break
    case 'down':
      aim += delta
      break
    case 'up':
      aim -= delta
      break
    default:
      throw('unsupported')
  }
})

console.log(x*y)