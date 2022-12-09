# f = open("example.txt", "r")
f = open("input.txt", "r")

# ingest grid
grid = []
while line := f.readline().rstrip():
    grid.append([int(v) for v in list(line)])
# print(grid)

# part 1
def isVisible(arr, i):
    return max(arr[:i] or [-1]) < arr[i] or max(arr[i+1:] or [-1]) < arr[i]

# determine visibility
# visGrid = []
# for y in range(len(grid)):
#     visRow = []
#     for x in range(len(grid[y])):
#         gridCol = [v[x] for v in grid]
#         xVis = isVisible(grid[y], x)
#         yVis = isVisible(gridCol, y)
#         visRow.append(int(xVis or yVis))

#     visGrid.append(visRow)
# print(visGrid)

# # count visible
# totalVis = sum([sum(v) for v in visGrid])
# print(totalVis)

# part 2
def numVisibleTreesDir(arr, height):
    count = 0
    arr2 = arr[:]
    while len(arr2) and (treeHeight:=arr2.pop(0)) <= height:
        count += 1
        if treeHeight == height:
            break
    return count

def ssArr(arr, i):
    a = numVisibleTreesDir(arr[:i][::-1], arr[i])
    b = numVisibleTreesDir(arr[i+1:], arr[i])
    return a * b

# scenic scores
topSS = -1
for y in range(len(grid)):
    for x in range(len(grid[y])):
        gridCol = [v[x] for v in grid]
        xSS = ssArr(grid[y], x)
        ySS = ssArr(gridCol, y)
        topSS = max(topSS, xSS * ySS)
print(topSS)