f = open("example.txt", "r")
f = open("input.txt", "r")

rules = dict()
while (line := f.readline().rstrip().split('|')) and len(line[0]):
    if line[0] not in rules:
        rules[line[0]] = []
    rules[line[0]].append(line[1])

def validatePages(pages, isCorrecting=False):
    prev = dict()
    i = 0
    hasReset = False
    while i < len(pages):
        page = pages[i]
        if page in rules:
            for match in rules[page]:
                if match in prev:
                    if not isCorrecting:
                        return 0
                    j = pages.index(match)
                    newPages = pages[:j] + pages[j+1:i+1] + [match] + pages[i+1:]

                    pages = newPages
                    prev = dict()
                    i = -1
                    hasReset = True
                    break

        if 0 <= i:
            prev[page] = True
        i += 1
    return int(pages[len(pages)//2]) if not isCorrecting or hasReset else 0

total = 0
while (pages := f.readline().rstrip().split(',')) and len(pages[0]):
    total += validatePages(pages, True)
print(total)
