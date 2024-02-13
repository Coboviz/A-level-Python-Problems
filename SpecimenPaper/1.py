TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(TheData):
    for i in range(1 , 9):
        DataToInsert = TheData[i]
        Inserted = 0
        NextValue = i - 1
        while (NextValue >= 0 and Inserted != 1):
            if (DataToInsert < TheData[NextValue]):
                TheData[NextValue+1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1




def Output(TheData):
    for item in TheData:
        print(item, " ", end="")
    print()

Output(TheData)

InsertionSort(TheData)

Output(TheData)

def InTheArray(TheData, SearchValue):
    for item in TheData:
        if item == SearchValue:
            print("found")
            return True
    print("not found")
    return False

InTheArray(TheData, 8)
InTheArray(TheData, 9)