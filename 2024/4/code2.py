f = open("example.txt", "r")
f = open("input.txt", "r")

grid = list()

while (line := list(f.readline().rstrip())) and len(line[0]):
    grid.append(line)

def scanTile(x, y)->int:
    a = grid[y-1][x-1] + grid[y+1][x+1]
    b = grid[y-1][x+1] + grid[y+1][x-1]

    return (a == 'MS' or a == 'SM') and (b == 'MS' or b == 'SM')

total = 0
for y in range(1, len(grid)-1):
    for x in range(1, len(grid[0])-1):
        if grid[y][x] == 'A':
            total += scanTile(x, y)
print(total)
