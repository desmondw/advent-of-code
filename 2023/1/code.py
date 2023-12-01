# f = open("example.txt", "r")
f = open("input.txt", "r")

NUMBERS = '1234567890'
total = 0

while (line := f.readline().rstrip()) and len(line):
    first = None
    second = None
    for i in range(len(line)):
        if not first and line[i] in NUMBERS:
            first = line[i]
        if not second and line[len(line)-1-i] in NUMBERS:
            second = line[len(line)-1-i]
        if first and second:
            break
    num = int(first + second)
    total += num

print(total)