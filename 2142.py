class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

startPointer = 0
emptyList = 5
linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7,-1),
              node(2, 2), node(0, 6), node(0, 8), node(56, 3),
              node(0, 9), node(0, -1)]

def outputNodes(linkedList, startPointer):
    currentPointer = startPointer
    while (currentPointer != -1):
        print(str(linkedList[currentPointer].data))
        currentPointer = linkedList[currentPointer].nextNode

outputNodes(linkedList, startPointer)

def addNode(linkedList, startPointer, emptyList):
    dataAdd = int(input())
    currentPointer = startPointer
    if emptyList < 0 or emptyList > 9:
        return False    
    newEmptyListPtr = linkedList[emptyList].nextNode
    newNode = node(int(dataAdd), -1)
    linkedList[emptyList] = newNode
    previousPointer = 0
    while (currentPointer != -1):
        previousPointer = currentPointer
        currentPointer = linkedList[previousPointer].nextNode
    linkedList[previousPointer].nextNode = emptyList
    emptyList = newEmptyListPtr
    return True

addNode(linkedList, startPointer, emptyList)

outputNodes(linkedList, startPointer)