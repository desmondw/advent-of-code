import pprint

f = open("example.txt", "r")
f = open("input.txt", "r")

total = 0
antennas = {}
y = 0
while (line := f.readline().rstrip()) and len(line):
    for (x, tile) in enumerate(line):
        if tile == '.': continue
        if tile not in antennas:
            antennas[tile] = []
        antennas[tile].append((x, y))
    y += 1

width = x+1
height = y

antinodes = {}
for antennaType in antennas.keys():
    nodes = antennas[antennaType]
    typeTotal = 0
    for i in range(len(nodes)):
        n1 = nodes[i]
        for j in range(i+1, len(nodes)):
            n2 = nodes[j]

            delta = (n2[0]-n1[0], n2[1]-n1[1])

            an1a = (n1[0], n1[1])
            while 0 <= an1a[0] < width and 0 <= an1a[1] < height:
                if an1a not in antinodes:
                    print(f'hit {antennaType} {an1a}')
                    antinodes[an1a] = True
                    typeTotal += 1
                an1a = (an1a[0]-delta[0], an1a[1]-delta[1])

            an1b = (n1[0]+delta[0], n1[1]+delta[1])
            while 0 <= an1b[0] < width and 0 <= an1b[1] < height:
                if an1b not in antinodes:
                    print(f'hit {antennaType} {an1b}')
                    antinodes[an1b] = True
                    typeTotal += 1
                an1b = (an1b[0]+delta[0], an1b[1]+delta[1])

            # if 0 <= an1[0] < width and 0 <= an1[1] < height:
            #     print(f'hit {antennaType} {an1}')
            #     if an1 not in antinodes:
            #         antinodes[an1] = True
            #         typeTotal += 1
            # if 0 <= an2[0] < width and 0 <= an2[1] < height:
            #     print(f'hit {antennaType} {an2}')
            #     if an2 not in antinodes:
            #         antinodes[an2] = True
            #         typeTotal += 1
    # n = len(nodes)-1
    # maxAntinodes = int(n*(n+1)/2)*2
    # print(f'type: {antennaType} nodes: {len(nodes)} antinodes: {typeTotal} (max antinodes: {maxAntinodes})')
    # if typeTotal > maxAntinodes:
    #     raise "woah nelly!"
    print('--')
print(f'{width}x{height} grid')
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(antinodes)

print(len(antinodes.keys()))