# f = open("example.txt", "r")
f = open("input.txt", "r")

def isUnique(arr):
    arr1 = arr[:]
    arr1.sort()
    arr2 = list(set(arr))
    arr2.sort()
    return arr1 == arr2

line = f.readline().rstrip()
# stack = list(line[:4]) # part 1
stack = list(line[:14]) # part 2

for i in range(4,len(line)):
    if isUnique(stack):
        print(i)
        break

    stack.pop(0)
    stack.append(line[i])
