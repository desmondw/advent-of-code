f = open("example.txt", "r")
f = open("input.txt", "r")

class Guard:
    def __init__(self, x:int, y:int, d:int=0):
        self.x = x
        self.y = y
        self.d = d # d: 0=up, 1=right, 2=down, 3=left
        self.turnHistory = [(self.x, self.y, self.d)]

    def turn(self):
        self.d = (self.d + 1) % 4
        self.turnHistory.append((self.x, self.y, self.d))

    def isOOB(self, rows):
        return not (0 <= self.x < len(rows[0]) and 0 <= self.y < len(rows))

    def isColliding(self, rows):
        return rows[self.y][self.x] == '#'

    def isAtOrigin(self):
        return self.x == self.turnHistory[0] and self.y == self.turnHistory[1]

    def wouldBeInLoop(self, rows, dx, dy):
        # setup
        tileState = rows[pos.y][pos.x]
        rows[pos.y][pos.x] = '#'

        # follow path until either OOB (False) or new turn matches a turn history temp (True)
        loopPos = Guard(self.x - dx, self.y - dy, self.d)
        loopPos.turnHistory = self.turnHistory[:]

        loopPos.turn()

        while True:
            dyl = loopPos.d - 1  if loopPos.d % 2 == 0 else 0
            dxl = -loopPos.d + 2 if loopPos.d % 2 == 1 else 0
            loopPos.y += dyl
            loopPos.x += dxl
            if loopPos.isOOB(rows):
                rows[pos.y][pos.x] = tileState
                return False
            if loopPos.isColliding(rows):
                loopPos.y -= dyl
                loopPos.x -= dxl
                loopPos.turn()

                # turn duplicate check
                if loopPos.turnHistory[-1] in loopPos.turnHistory[:-1]:
                    rows[pos.y][pos.x] = tileState
                    return True

rows = []
pos:Guard
while (row := [x for x in f.readline().rstrip()]) and len(row[0]):
    if '^' in row:
        pos = Guard(row.index('^'), len(rows))
        # pos.x = row.index('^')
        # pos.y = len(rows)
        row[pos.x] = 'X'
    rows.append(row)

total = 1
total2 = 0
while True:
    dy = pos.d - 1  if pos.d % 2 == 0 else 0
    dx = -pos.d + 2 if pos.d % 2 == 1 else 0

    pos.y += dy
    pos.x += dx
    if pos.isOOB(rows):
        break

    if pos.isColliding(rows):
        pos.y -= dy
        pos.x -= dx
        pos.turn()
    else:
        # walk
        if rows[pos.y][pos.x] == '.':
            total += 1

        # obstruction loop?
        if rows[pos.y][pos.x] == '.' and not pos.isAtOrigin() and pos.wouldBeInLoop(rows, dx, dy):
            total2 += 1
            rows[pos.y][pos.x] = 'O'

        # mark
        if rows[pos.y][pos.x] == '.':
            rows[pos.y][pos.x] = 'X'


# print(f'grid: {len(rows)} rows, {len(rows[0])} cols')
# for row in rows:
#     print(''.join(row))


print(total)
print(total2)

# oCount = 0
# for row in rows:
#     oCount += row.count('O')
# print(f'num of "O"s: {oCount}')
# print(f'origin: {pos.turnHistory[0]}')
# print(rows[pos.turnHistory[0][1]][pos.turnHistory[0][0]])