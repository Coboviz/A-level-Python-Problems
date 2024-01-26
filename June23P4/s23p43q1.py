DataArray = [] # Data array consists of 25 zeroes

FileName = "Data.txt"

try:
    File = open(FileName, "r")
    for line in File:
        DataArray.append(int(line))
    File.close()
except IOError:
    print("No such file")

def PrintArray(DataArray):
    for x in DataArray:
        print(str(x) + " ", end = "")

PrintArray(DataArray)
print()
def LinearSearch(DataArray, ValueWeLookFor):
    count = 0
    for x in DataArray:
        if x == ValueWeLookFor:
            count = count + 1
    return count

userInput = int(input("Input a number between 0 and a 100: \n"))

if userInput < 0 or userInput > 100:
    print("Number you entered is out of bounds") 
else:
    retVal = LinearSearch(DataArray, userInput)
    print(f"The number {userInput} is found {retVal} times")


