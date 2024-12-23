from functools import reduce

f = open("example.txt", "r")
f = open("input.txt", "r")

def checkOps(terms, result):
    if len(terms) <= 0:
        return False
    if len(terms) == 1:
        return result == terms[0]

    return  checkOps([terms[0]+terms[1]] + terms[2:], result) or \
            checkOps([terms[0]*terms[1]] + terms[2:], result) or \
            checkOps([int(str(terms[0])+str(terms[1]))] + terms[2:], result)

total = 0
i=0
while (line := f.readline().rstrip().split(': ')) and len(line[0]):
    i+=1
    result = int(line[0])
    terms = [int(x) for x in line[1].split(' ')]
    # print(f'loop start {i} | result: {result} | terms: {terms}')

    if checkOps(terms, result):
        total += result

print(total)