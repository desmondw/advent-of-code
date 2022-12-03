# f = open("example.txt", "r")
f = open("input.txt", "r")

#  part 1
# sum = 0
# while line := f.readline():
#     line = line.strip()
#     iHalf = int(len(line)/2)
#     ruck = [line[:iHalf], line[iHalf:]]

#     for c in ruck[0]:
#         if c in ruck[1]:
#             priority = ord(c)
#             priority -= 96 if c == c.lower() else 38
#             sum += priority
#             break
# print(sum)


# part 2
sum = 0
rucks = []
while line := f.readline():
    rucks.append(line.strip())
    rucks.append(f.readline().strip())
    rucks.append(f.readline().strip())

    for c in rucks[0]:
        if not (c in rucks[1] and c in rucks[2]):
            continue
        priority = ord(c)
        priority -= 96 if c == c.lower() else 38
        sum += priority

        rucks = []
        break
print(sum)

