# ID, MaxSpeed, CurrentSpeed, IncreaseAmount, HorizontalPosition

# ID : STRING
# MaxSpeed : INTEGER
# CurrentSpeed : INTEGER, 
# IncreaseAmount : INTEGER
# HorizontalPosition : INTEGER

class Vechile:
    def __init__(self, ID, MaxSpeed, CurrentSpeed, IncreaseAmount, HorizontalPosition):
        self.__ID = ID # string
        self.__MaxSpeed = MaxSpeed # int
        self.__CurrentSpeed = CurrentSpeed # int 
        self.__IncreaseAmount = IncreaseAmount # int 
        self.__HorizontalPosition = HorizontalPosition # int

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed 
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def SetCurrentSpeed(self, NewCurrentSpeed):
        self.__CurrentSpeed = NewCurrentSpeed

    def SetHorizontalPosition(self, NewHorizontalPosition):
        self.__HorizontalPosition = NewHorizontalPosition

    def InreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

# VerticalPostion : INTEGER
# VerticalChange : INTEGER
# MaxHeight : INTEGER
class Helicopter(Vechile):
    def __init__(self, ID, MaxSpeed, CurrentSpeed, IncreaseAmount, HorizontalPosition, VerticalPosition, VerticalChange, MaxHeight):
        Vechile.__init__(self, ID, MaxSpeed, CurrentSpeed, IncreaseAmount, HorizontalPosition)
        self.VerticalPosition = VerticalPosition # int
        self.VerticalChange = VerticalChange # int
        self.MaxHeight = MaxHeight

    #OVERRIDE

    def InreaseSpeed(self):
        self.VerticalPosition = self.VerticalPosition + self.VerticalChange
        if self.VerticalPosition > self.MaxHeight:
            self.VerticalPosition = self.MaxHeight

        self.SetCurrentSpeed(self.GetCurrentSpeed() + self.GetIncreaseAmount())
        if self.GetCurrentSpeed() > self.GetMaxSpeed():
            self.SetCurrentSpeed(self.GetMaxSpeed())
        self.SetHorizontalPosition(self.GetHorizontalPosition() + self.GetCurrentSpeed())

def OutputInfo(argVechile):
    heli = Helicopter("", 0, 0, 0, 0, 0, 0, 0)
    vechi = Vechile("", 0, 0, 0, 0)
    if type(argVechile) == type(vechi):
        print(f"Horizontal position of this vechile: {argVechile.GetHorizontalPosition()}, speed of this vechile is: {argVechile.GetCurrentSpeed()}")
    
    if type(argVechile) == type(heli):
        print(f"Horizontal position of this vechile: {argVechile.GetHorizontalPosition()}, speed of this vechile is: {argVechile.GetCurrentSpeed()}, current vertical position is: {argVechile.VerticalPosition}")


car = Vechile("Tiger", 100, 0, 20, 0)
heli = Helicopter("Lion", 350, 0, 40, 0, 3, 0, 100)

car.InreaseSpeed()
car.InreaseSpeed()

OutputInfo(car)

heli.InreaseSpeed()
heli.InreaseSpeed()

OutputInfo(heli)


# If you use private attributes in parent class, be sure to access those values using setters in the child class
# If you need to change values in an object of a parent class use setters, don't access immidietaly

# If you want to check a type of a variable use function type, e.g. print(type("thisisastring")) : string

# to compare types - just create empty variables of those class types and you can check what are they quite easily