# f = open("example.txt", "r")
f = open("input.txt", "r")

def winPoints(a, b):
    draw = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    }
    if draw[a] == b:
        return 3

    x = a == 'A' and b == 'Y'
    y = a == 'B' and b == 'Z'
    z = a == 'C' and b == 'X'
    return 6 if x or y or z else 0

def winPointsV2(a, b):
    hand = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    return hand[b]

def actionPointsV2(a, b):
    draw = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    }
    loss = {
        'B': 'X',
        'C': 'Y',
        'A': 'Z',
    }
    win = {
        'C': 'X',
        'A': 'Y',
        'B': 'Z',
    }
    hand = {
        'X': loss[a],
        'Y': draw[a],
        'Z': win[a],
    }
    return hand[b]


score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

total = 0

while line := f.readline():
    (a, b) = line.strip().split(' ')
    # total += score[b] + winPoints(a, b)
    total += score[actionPointsV2(a, b)] + winPointsV2(a, b)
print(total)