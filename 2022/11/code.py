# f = open("example.txt", "r")
f = open("input.txt", "r")

class Monkey():
    def __init__(self, id, monkeys, items, fnWorry, fnPass):
        self.id      = id
        self.monkeys = monkeys
        self.items   = items
        self.fnWorry = fnWorry
        self.fnPass  = fnPass

        self.comDenom = 1
        self.inspects = 0

    def __str__(self):
        return f'#{self.id}, items: {self.items},\n  sampleFnWorry: {self.fnWorry(100)},\tsampleFnPass: {self.fnPass(100)}'

    def run(self):
        self.inspects += len(self.items)
        for item in self.items:
            item = self.fnWorry(item) % self.comDenom
            newMonkeyId = self.fnPass(item)
            self.monkeys[newMonkeyId].receive([item])
        self.items = []

    def receive(self, items):
        self.items += items

ROUNDS = 10000
monkeys = []
comDenom = 1

# input parsing
while line := f.readline():
    # new monkey
    items   = [int(x) for x in f.readline().strip().split(': ')[1].split(', ')]

    fnWorryOp = f.readline().strip().split(': ')[1].split(' = ')[1]
    fnWorry = eval(f'lambda old: {fnWorryOp}')

    fnPassA = int(f.readline().strip().split(': ')[1].split(' ')[-1])
    fnPassB = int(f.readline().strip().split(': ')[1].split(' ')[-1])
    fnPassC = int(f.readline().strip().split(': ')[1].split(' ')[-1])
    fnPass = eval(f'lambda v: {fnPassC} if v % {fnPassA} else {fnPassB}')
    comDenom *= fnPassA

    monkey = Monkey(len(monkeys), monkeys, items, fnWorry, fnPass)
    monkeys.append(monkey)
    line = f.readline()

# set common denominator
for monkey in monkeys:
    monkey.comDenom = comDenom

# execution
for i in range(ROUNDS):
    for monkey in monkeys:
        monkey.run()

# calculating monkey business
allInspects = []
for monkey in monkeys:
    allInspects.append(monkey.inspects)
allInspects.sort()
print(allInspects[-2] * allInspects[-1])