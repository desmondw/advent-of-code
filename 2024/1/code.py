f = open("example.txt", "r")
f = open("input.txt", "r")

left = list()
right = list()
freq = dict()

while (line := f.readline().rstrip().split('   ')) and len(line[0]):
    left.append(l:=int(line[0]))
    right.append(r:=int(line[1]))

    if r not in freq:
        freq[r] = 0
    freq[r] += 1

left.sort()
right.sort()

total = 0
total2 = 0
for i in range(len(left)):
    total += abs(right[i] - left[i])
    if left[i] in freq:
        total2 += left[i] * freq[left[i]]

print(total)
print(total2)
