f = open("example.txt", "r")
f = open("input.txt", "r")

# returns True if safe
def validateReport(levels: list, isRerun=False, minStep=1, maxStep=3)->bool:
    if len(levels) < 2:
        return False
    # check all levels increasing or all levels decreasing
    # check all steps between levels are within variance
    hasDecreased = False
    hasIncreased = False
    failed = False
    step = 0
    for i in range(1, len(levels)):
        step = int(levels[i]) - int(levels[i-1])
        if   step < 0: hasDecreased = True
        elif 0 < step: hasIncreased = True
        else:
            failed = True

        if hasIncreased and hasDecreased:
            failed = True

        if abs(step) < minStep or maxStep < abs(step):
            failed = True

        if failed:
            if isRerun:
                return False
            return  validateReport(levels[:i-1]+levels[i:], True) or \
                    validateReport(levels[:i]+levels[i+1:], True) or \
                    (0 <= i-2 and validateReport(levels[:i-2]+levels[i-1:], True))

    return True


totalSafe = 0
while (line := f.readline().rstrip().split(' ')) and len(line[0]):
    totalSafe += int(validateReport(line))

print(totalSafe)