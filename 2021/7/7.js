const fs = require('fs')

let data = fs.readFileSync('example.txt', 'utf8')
data = fs.readFileSync('input.txt', 'utf8')
// console.log(data)

let crabs = []
let sum = 0
data = data.split(',').map(v=>{v=+v; crabs[v]=(crabs[v]??0)+1; sum+=v; return v})

const getFuelCost = n => {
  return n * (n + 1) / 2
}

// TODO - MEMOIZE
const getFuelCosts = crabs => {
  let fuelCosts = []
  for (let i=0; i<crabs.length; i++){
    let left = crabs.slice(0,i).reverse().reduce((a,v,offset)=>a + (v??0)*getFuelCost(offset+1), 0)
    let right = crabs.slice(i+1).reduce((a,v,offset)=>a + (v??0)*getFuelCost(offset+1), 0)
    fuelCosts[i] = left + right
  }
  return fuelCosts
}

fuelCostsPart1 = getFuelCosts(crabs)
console.log(fuelCostsPart1)
console.log(Math.min(...fuelCostsPart1))
