# f = open("example.txt", "r")
# f = open("example2.txt", "r")
f = open("input.txt", "r")

# NOTE: using gamedev coord (up and left are negative)
ROPE_LENGTH = 10
rope = []
for i in range(ROPE_LENGTH):
    rope.append({'x':0,'y':0})
tailHistory = set()
tailHistory.add(str(rope[-1]))

def sign(n):
    return int(n/abs(n)) if n else 0

def moveHead(dir, head):
    if   dir == 'L': head['x'] -= 1
    elif dir == 'R': head['x'] += 1
    elif dir == 'U': head['y'] -= 1
    elif dir == 'D': head['y'] += 1
    else           : raise 'uh-oh'

def moveTail(head, tail):
    lead = {'x': head['x'] - tail['x'], 'y': head['y'] - tail['y']}

    # update tail
    if abs(lead['x']) >= 2 or abs(lead['y']) >= 2:
        tail['x'] += sign(lead['x'])
        tail['y'] += sign(lead['y'])

while (line := f.readline().rstrip().split(' ')) and len(line[0]):
    for i in range(int(line[1])):
        moveHead(line[0], rope[0])
        for i in range(1, len(rope)):
            moveTail(rope[i-1], rope[i])
        tailHistory.add(str(rope[-1]))

print(len(tailHistory))