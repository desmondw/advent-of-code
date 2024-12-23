const fs = require('fs')

let data
data = fs.readFileSync('example.txt', 'utf8')
// data = fs.readFileSync('input.txt', 'utf8')

for (line of data.split('\n')) {
  line = line.trimRight().split(/\s+/)
  continue
}