class Picture:
    def __init__(self, Description, Width, Height, FrameColour):
        self.__Description = Description # STRING
        self.__Width = Width # INTEGER
        self.__Height = Height # INTEGER
        self.__FrameColour = FrameColour # STRING
    
    # Double underscore -> private attribute

    def getDescription(self):
        return self.__Description
    
    def getWidth(self):
        return self.__Width
    
    def getHeight(self):
        return self.__Height
    
    def getFrameColour(self):
        return self.__FrameColour
    
    def SetDescription(self, NewDescription):
        self.__Description = NewDescription

PictureList = []
for i in range(0, 100):
    PictureList.append(Picture("", 0, 0, ""))

def ReadData(PictureList):
    FileName = "Pictures.txt"
    count = 0
    try:
        File = open(FileName, "r")
        Description = File.readline().strip() # a way to read a line in python
        while (Description != ""):
            Width = int(File.readline().strip())
            Height = int(File.readline().strip())
            FrameColour = File.readline().strip()
            PictureList[count] = Picture(Description, Width, Height, FrameColour)
            count = count + 1
            Description = File.readline().strip()
        File.close()
    except IOError:
        print("File doesn't exist")
    return count

numberOfElements = ReadData(PictureList)

for i in range (int(numberOfElements)):
    print(PictureList[i].getDescription())