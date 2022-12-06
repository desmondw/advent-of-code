# f = open("example.txt", "r")
f = open("input.txt", "r")

deck = []
while (line := f.readline().rstrip()) and len(line):
    deck.append(line)

deckLength = int(deck.pop().split(' ')[-1])

stacks = [[] for i in range(deckLength)]
while len(deck):
    level = deck.pop()

    for i in range(1, deckLength*4, 4):
        if i < len(level) and level[i] != ' ':
            idx = int((i-1)/4)
            stacks[idx].append(level[i])

while line := f.readline().rstrip():
    line = line.split(' ')
    amount   = int(line[1])
    moveFrom = int(line[3]) - 1
    moveTo   = int(line[5]) - 1

    boxes            = stacks[moveFrom][-amount:]
    stacks[moveFrom] = stacks[moveFrom][:-amount]
    # stacks[moveTo]   += boxes[::-1]  # part 1
    stacks[moveTo]   += boxes  # part 2

print(''.join([x[-1] for x in stacks]))
