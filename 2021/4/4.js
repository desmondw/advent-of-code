const fs = require('fs')

let data = fs.readFileSync('example.txt', 'utf8')
data = fs.readFileSync('input.txt', 'utf8')

let boards = data.split('\n\n')
let draws = boards.shift().split(',').map(v=>+v)

boards = boards.map(board=>{
  let lines = board.split('\n')
  lines = lines.map(line=>line.trim().split(/\s+/).map(v=>+v))
  return lines
})

console.log(draws)
// console.log(boards)
console.log('---')

/// functions

const markBoard = (board, hit) => {
  board.forEach((line,i)=>{
    line.forEach((v,j)=>{
      if (board[i][j] === hit)
        board[i][j] = null
    })
  })
}
const checkBoard = (board) => {
  for (let i=0; i<board[0].length;i++){
    if (board[i].every(v=>v===null)) return true
    let vert = []
    for (let j=0; j<board[0].length;j++){
      vert.push(board[j][i])
    }
    if (vert.every(v=>v===null)) return true
  }
  return false
}
const countBoard = (board) => {
  return board.reduce((aLine,line)=>{
    return aLine + line.reduce((a,v)=>a+(v??0),0)
  },0)
}

/// work
const markAndCheckBoards = (boards) =>{
  let winningCounts = []
  for (let j=0; j<draws.length;j++){
    let nextBoards = []
    for (let i=0; i<boards.length;i++){
      let board = boards[i]
      let hit = draws[j]
      markBoard(board, hit)
      if (checkBoard(board)) {
        console.log(board)
        // return countBoard(board) * hit
        winningCounts.push(countBoard(board) * hit)
      } else {
        nextBoards.push(board)
      }
    }
    boards = nextBoards
  }
  return winningCounts.pop()
}

console.log(markAndCheckBoards(boards))
