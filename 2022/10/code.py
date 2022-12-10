# f = open("example.txt", "r")
f = open("input.txt", "r")


FREQ = 40
SIGNAL_CAP = 6

class Assembler():
    def __init__(self, file, freqStart=0):
        self.freqStart = 0
        self.file = file
        self.register = 1
        self.cycle = 0
        self.scanline = ''

        self.signals = []
        self.scanlines = []

    def addToReg(self, v):
        self.register += v

    def getCol(self):
        return ((self.cycle + self.freqStart) % FREQ)

    def drawPixel(self):
        self.scanline += '#' if abs(self.register - self.getCol()) <= 1 else '.'

    def runCycle(self):
        self.drawPixel()
        self.cycle += 1

        if self.getCol() == 0:
            self.signals.append(self.cycle * self.register)

            self.scanlines.append(self.scanline)
            self.scanline = ''


    def run(self):
        while (line := self.file.readline().rstrip().split(' ')) and len(line[0]):
            if line[0] == 'noop':
                self.runCycle()
            elif line[0] == 'addx':
                self.runCycle()
                self.runCycle()
                self.addToReg(int(line[1]))
            else:
                raise 'zoinks!'

    def printPart1(self):
        print(sum(self.signals))

    def printPart2(self):
        for scanline in self.scanlines:
            print(scanline)

# ass = Assembler(f, 20)
# ass.run()
# ass.printPart1()

ass = Assembler(f, 20)
ass.run()
ass.printPart2()
