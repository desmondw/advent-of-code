f = open("example.txt", "r")
# f = open("input.txt", "r")

while (line := f.readline().rstrip().split(' ')) and len(line[0]):
    pass
