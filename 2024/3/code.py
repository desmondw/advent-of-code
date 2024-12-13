f = open("example.txt", "r")
f = open("example2.txt", "r")
f = open("input.txt", "r")

text = f.read().rstrip()
dos = text.split("do()")
for i in range(len(dos)):
    dos[i] = dos[i].split("don't()")[0]
# print(dos)
# print(len(dos))
text = ''.join(dos)


# print(text)

import re
mults = re.findall(r'mul\((\d+),(\d+)\)', text)
# print(mults)

total = 0
for a, b in mults:
    total += int(a) * int(b)

print(total)