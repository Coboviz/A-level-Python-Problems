#CLASS HiddenBox
    # __BoxName : PRIVATE STRING
    # __Creator : PRIVATE STRING
    # __DateHidden : PRIVATE STRING
    # __GameLocation : PRIVATE STRING
    # __LastFinds : PRIVATE ARRAY[][] OF STRING
    # __Active : PRIVATE BOOLEAN
 #ENDCLASS

class HiddenBox:
    def __init__(self, BoxName, Creator, DateHidden, GameLocation):
        self.__BoxName = BoxName
        self.__Creator = Creator
        self.__DateHidden = DateHidden
        self.__GameLocation = GameLocation 
    
    def GetBoxName(self):
        return self.__BoxName
    
    def getGameLocation(self):
        return self.__GameLocation
    
    #def str(self):
        #return self.__BoxName + " " + self.__Creator + " " + self.__DateHidden + " " + self.__GameLocation
    
TheBoxes = []

#for i in range(10000):
#   TheBoxes.append({"", "", "", ""})

def NewBox(Name, Creator, DateHidden, GameLocation):
    TheBoxes.append(HiddenBox(Name, Creator, DateHidden, GameLocation))

NewBox("Test", "Test", "Test", "Test")

class PuzzleBox(HiddenBox):
    def __init__(self, PuzzleText, Solution, BoxName, Creator, DateHidden, GameLocation):
        super().__init__(self, BoxName, Creator, DateHidden, GameLocation)
        self.__PuzzleText = PuzzleText
        self.__Solution = Solution

