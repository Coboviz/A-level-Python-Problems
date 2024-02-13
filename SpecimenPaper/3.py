QueueData = ["" for i in range (20)]
StartPointer = -1
EndPointer = -1

def Enqueue(Item):
    global QueueData
    global StartPointer
    global EndPointer
    if StartPointer == -1:
        StartPointer = 0
        EndPointer = 0
        QueueData[0] = Item
        return True
    else:
        if EndPointer == 19:
            return False
        else:
            EndPointer = EndPointer + 1
            QueueData[EndPointer] = Item
            return True
        
def ReadFile():
    global QueueData
    global StartPointer
    global EndPointer
    FileName = input("Enter the File name: ")

    try:
        File = open(FileName, "r")
        
        for line in File:
            TruthVal = Enqueue(line)
            if not TruthVal:
                print("Full queue")
                File.close()
                return 1
            
        print("Everything is fine don't worry")
        File.close()
        return 2
    except IOError:
        print("File doesn't exist")
        return -1
    
ReadFile()

def Remove():
    global QueueData
    global StartPointer
    global EndPointer
    if StartPointer == EndPointer:
        return "No items"
    prevStartPointer = StartPointer
    StartPointer = StartPointer - 2
    return QueueData[prevStartPointer].strip() + " " + QueueData[prevStartPointer + 1].strip()

            
ret = Remove()

print(ret)