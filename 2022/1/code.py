# f = open("example.txt", "r")
f = open("input.txt", "r")


top = 0
counts = []

count = 0
while line := f.readline():

    if line == '\n':
        top = max(top, count)
        counts.append(count)
        count = 0
    else:
        count += int(line)
        # print(int(line))

print(top)
counts.sort()
top3 = counts[-3:]
print(sum(top3))