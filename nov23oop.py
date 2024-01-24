class Charachter:
    def __init__(self, Name, XPosition, YPosition):
        self.Name = Name # STRING
        self.XPosition = XPosition # INTEGER
        self.YPosition = YPosition # INTEGER

    def getXPosition(self):
        return self.XPosition
    
    def getYPosition(self):
        return self.YPosition
    
    def setXPosition(self, x):
        self.XPosition = self.XPosition + x
        if self.XPosition > 10000:
            self.XPosition = 10000
        if self.XPosition < 0:
            self.XPosition = 0
        

    def setYPosition(self, y):
        self.YPosition = self.YPosition + y
        if self.YPosition > 10000:
            self.YPosition = 10000
        if self.YPosition < 0:
            self.YPosition = 0
        

    def Move(self, command):
        if command == "up":
            self.setYPosition(10)
        if command == "down":
            self.setYPosition(-10)
        if command == "right":
            self.setXPosition(10)
        if command == "left":
            self.setXPosition(-10)

NewCharachter = Charachter("Jack", 50, 50)

class BikeCharachter(Charachter):
    def __init__(self, Name, XPosition, YPosition):
        super().__init__(Name, XPosition, YPosition)

    #override
        
    def Move(self, command):
        if command == "up":
            self.setYPosition(20)
        if command == "down":
            self.setYPosition(-20)
        if command == "right":
            self.setXPosition(20)
        if command == "left":
            self.setXPosition(-20)

NewBikeCharachter = BikeCharachter('Karla', 100, 100)

charachterName = input("Which charachrer would you like to move?")
charachterDirection = input("In which direction?")

if charachterName == "Karla":
    NewBikeCharachter.Move(charachterDirection)
    print(f"Karla's new position is X  = {NewBikeCharachter.getXPosition()} Y = {NewBikeCharachter.getYPosition}")
else:
    NewCharachter.Move(charachterDirection)
    print(f"Jack's new position is X  = {NewCharachter.getXPosition()} Y = {NewCharachter.getYPosition}")
    
