# f = open("example.txt", "r")
f = open("input.txt", "r")

def checkContains(a, b):
    x = a[0] <= b[0] and b[1] <= a[1]
    y = b[0] <= a[0] and a[1] <= b[1]
    return x or y

def checkOverlaps(a, b):
    x = a[0] <= b[1] and b[0] <= a[1]
    y = b[0] <= a[1] and a[0] <= b[1]
    return x or y

total = 0
while line := f.readline().rstrip():
    (elf1, elf2) = line.split(',')
    elf1 = [int(x) for x in elf1.split('-')]
    elf2 = [int(x) for x in elf2.split('-')]


    # if checkContains(elf1, elf2) or checkContains(elf2, elf1):
    #     total += 1
    if checkOverlaps(elf1, elf2) or checkOverlaps(elf2, elf1):
        total += 1

print(total)
