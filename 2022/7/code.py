# f = open("example.txt", "r")
f = open("input.txt", "r")

# directory nodes
class Node():
    def __init__(self, name, size=None):
        self.name = name
        self.size = size
        self.parent = None
        self.children = []

    def __str__(self):
        return f'{self.size or 0} {self.name}'

    def addChild(self, child):
        if child.name not in [v.name for v in self.children]:
            child.parent = self
            self.children.append(child)
            return True
        return False

    def getSize(self):
        if self.size is not None:
            return self.size

        return sum([x.getSize() for x in self.children])

MAX_SPACE = 70000000
REQ_SPACE = 30000000
rootNode = Node('/')
curDir = rootNode
directories = [rootNode]

# burn header excess
f.readline()

# build out directory structure
while (line := f.readline().rstrip().split(' ')) and len(line[0]):
    if line[0] == '$':
        if line[1] != 'cd': continue

        # changing directory
        cd = line[2]
        if cd == '/':
            curDir = rootNode
        elif cd == '..':
            curDir = curDir.parent or rootNode
        else:
            curDir = [x for x in curDir.children if x.name == cd][0]
    else:
        # check-adding child dir / file
        size = int(line[0]) if line[0] != 'dir' else None
        name = line[1]

        child = Node(name, size)
        if curDir.addChild(child) and not size:
            directories.append(child)

# part 1
answer = sum([dirSize for dir in directories if (dirSize:=dir.getSize()) <= 100000])
print(answer)

# part 2
spaceUsed = rootNode.getSize()
unusedSpace = MAX_SPACE - spaceUsed
spaceNeeded = REQ_SPACE - unusedSpace

dirsToDelete = [dirSize for dir in directories if (dirSize:=dir.getSize()) >= spaceNeeded]
print(min(dirsToDelete))