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

linea = []
for antennaType in antennas.keys():
    nodes = antennas[antennaType]
    typeTotal = 0
    for i in range(len(nodes)):
        n1 = nodes[i]
        for j in range(i+1, len(nodes)):
            n2 = nodes[j]

            delta = (n1[0]-n2[0], n1[1]-n2[1])
            rate = delta[1]/delta[0]
            delta = (rate, n1[0]*-rate+n1[1])
            linea.append(delta)

print(f'{width}x{height} grid')
print(f'linea| {linea}')

total = 0
for x in range(width):
    for y in range(height):
        # y = x * delta[0] + delta[1]
        total += int(any(y == x * lx + ly for (lx,ly) in linea))

print(total)