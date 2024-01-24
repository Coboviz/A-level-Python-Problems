class TreasureChest:
    #question : STRING
    #answer : INTEGER
    #points : INTEGER
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points # double underscore for private attributes
    
    def getQuestio(self):
        return self.__question
    
    def checkAnswer(self, userAnswer):
        return self.__answer == userAnswer
    
    def getPoints(self, numberOfAttempts):
        if numberOfAttempts == 1:
            return self.__points


def readData():
    fileName = 'TreasureChest.txt'
    #arrayTreasure : TreasureChest
    arrayTreasure = []
    try:
        file = open(fileName, 'r')
        dataRead = file.readline().strip() #removes spaces and newlines
        while (dataRead != ''):
            question = dataRead
            answer = file.readline().strip()
            points = file.readline().strip()
            arrayTreasure.append(TreasureChest(question, answer, points))
            dataRead = file.readline().strip()
        file.close()
    except IOError:
        print('File not found')