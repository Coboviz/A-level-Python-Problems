headOfList = 0

value = [4, 3, 7, 11, 9]
nextNodes = [-1, -1, -1, -1, -1]


listLength = len(value)
lastIndex = 0

for i in range (listLength):
    nextNodes[i] = i + 1
    lastIndex = i
    if (i == listLength - 1):
        nextNodes[i] = -1
        lastIndex = i

print(value)
print(nextNodes)

print()

def appendNode(newVal):
    global listLength
    value.append(newVal)
    nextNodes.append(-1)
    nextNodes[lastIndex] =  lastIndex+1
    listLength += 1

appendNode(7)

print(value)
print(nextNodes)

print()

def removeElement(valueToRemove):
    for i in range (listLength):
        if (value[i] == valueToRemove):
            nextNodes[i-1] = nextNodes[i]
            nextNodes[i] = -2

removeElement(3)

print(value)
print(nextNodes)

print()

def iterateList():
    global headOfList
    for i in range(listLength):
        if (headOfList == -2):
            headOfList = nextNodes[i]
        else:
            print(value[headOfList], " ", end = "")
            headOfList = nextNodes[i]   
    headOfList = 0     

iterateList()

