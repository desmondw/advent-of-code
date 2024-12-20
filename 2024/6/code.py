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

    def isInLoop(self, rows):
        # follow path until either OOB (False) or new turn matches a turn history temp (True)
        loopPos = Guard(self.x, self.y, self.d)
        loopPos.turnHistory = self.turnHistory[:]

        loopPos.turn()

        while True:
            dyl = loopPos.d - 1  if loopPos.d % 2 == 0 else 0
            dxl = -loopPos.d + 2 if loopPos.d % 2 == 1 else 0
            loopPos.y += dyl
            loopPos.x += dxl
            if loopPos.isOOB(rows):
                return False
            if loopPos.isColliding(rows):
                loopPos.y -= dyl
                loopPos.x -= dxl
                loopPos.turn()

                # turn duplicate check
                if loopPos.turnHistory[-1] in loopPos.turnHistory[:-1]:
                    return True

rows = []
pos = Guard(-1, -1)
while (row := [x for x in f.readline().rstrip()]) and len(row[0]):
    if '^' in row:
        pos.x = row.index('^')
        pos.y = len(rows)
        row[pos.x] = 'X'
    rows.append(row)
    # print(row)
# print(f'grid loaded: {len(rows)} rows, {len(rows[0])} cols')

total = 1
total2 = 0
while True:
    dy = pos.d - 1  if pos.d % 2 == 0 else 0
    dx = -pos.d + 2 if pos.d % 2 == 1 else 0
    # oldPos = (pos.x, pos.y)

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
        if rows[pos.y][pos.x] != 'O' and not pos.isAtOrigin():
            # setup
            tileState = rows[pos.y][pos.x]
            rows[pos.y][pos.x] = '#'
            pos.y -= dy
            pos.x -= dx

            # test loop
            isLoop = pos.isInLoop(rows)

            # revert setup
            pos.y += dy
            pos.x += dx
            rows[pos.y][pos.x] = tileState

            # loop follow-up
            if isLoop:
                total2 += 1
                rows[pos.y][pos.x] = 'O'

        # if len(pos.turnHistory) >= 3:
        #     yLoop = pos.d % 2 == 0 and pos.y - dy == pos.turnHistory[-3][1]
        #     xLoop = pos.d % 2 == 1 and pos.x - dx == pos.turnHistory[-3][0]
        #     if (xLoop or yLoop) and rows[pos.y][pos.x] != 'O' and not pos.isAtOrigin():
        #         total2 += 1
        #         rows[pos.y][pos.x] = 'O'

        # for more complex obstruction loops...
            # check w/ above logic against ALL pos.turnHistory[0:-2]
            # (also missing:)
                # 1) if there's a native obstruction in the way after the turn (on an unwalked path)
              # 2) need to test and project a turn line for EVERY step to see if I hit:
                    # a) a T-intersection (wall parallel to previous path)
                    # b) could introduce a completely new loop, separate from previous paths

        # mark
        if rows[pos.y][pos.x] == '.':
            rows[pos.y][pos.x] = 'X'

    # print(f'oldPos: {oldPos[0]},{oldPos[1]} [{rows[oldPos[1]][oldPos[0]]}] | newPos: {pos.x},{pos.y}')
    # print(f'oldPos: {oldPos[0]},{oldPos[1]} [{rows[oldPos[1]][oldPos[0]]}] | newPos: {pos.x},{pos.y} [{rows[pos.y][pos.x]}]')

# for row in rows:
#     print(''.join(row))


print(total)
print(total2)