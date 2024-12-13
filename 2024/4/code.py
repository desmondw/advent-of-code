f = open("example.txt", "r")
f = open("input.txt", "r")

grid = list()

while (line := list(f.readline().rstrip())) and len(line[0]):
    grid.append(line)

def scanDirection(x, y, xd, yd, wordTail):
    if len(wordTail) == 0:
        return 1

    x += xd
    y += yd
    if x < 0 or len(grid[0]) <= x or y < 0 or len(grid) <= y:
        # out of bounds
        return 0
    if wordTail[0] != grid[y][x]:
        return 0

    return scanDirection(x, y, xd, yd, wordTail[1:])

# returns # of matches
def scanTile(x, y, word)->int:
    if grid[y][x] != word[0]:
        return 0
    matches = 0
    for i in range(-1,2):
        for j in range(-1,2):
            # MAY check here if grid isn't long enough, to save cycles
            matches += scanDirection(x, y, i, j, word[1:])
    return matches

total = 0
for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        total += scanTile(x, y, 'XMAS')
print(total)
