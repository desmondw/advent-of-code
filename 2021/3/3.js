const fs = require('fs')

const flip = (v, digits) => ~v & (2**digits - 1)

// let data = fs.readFileSync('example.txt', 'utf8').split('\n')
let data = fs.readFileSync('input.txt', 'utf8').split('\n')
// console.log(data)



const getFreqBinary = nums => {
  let freq = nums.reduce((a,num)=>{
    return a.map((v,i)=>v+ +num[i])
  }, Array(nums[0].length).fill(0))
  let freqBinary = freq.map(v=>(v>=nums.length/2)?1:0).join('')
  return freqBinary
}


let gamma = parseInt(getFreqBinary(data), 2)
let epsilon = flip(gamma, data[0].length)
let result = gamma * epsilon
console.log(result)
console.log('----')

// part 2
// TODO: the request is actually for the frequency of the bit column for the REMAINING binaries not removed

const getRating = (nums, isOxygen) => {
  let bitLength = nums[0].length
  for (let i=0;i<bitLength;i++) {
    let freqBinary = getFreqBinary(nums)
    nums = nums.filter(num => isOxygen ? num[i]===freqBinary[i] : num[i]!==freqBinary[i])
    if (nums.length === 1) {
      return parseInt(nums[0], 2)
    }
  }
}

let oxygenRating = getRating(data, true)
let carbonRating = getRating(data, false)

console.log(oxygenRating * carbonRating)
