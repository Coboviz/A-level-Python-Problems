print("Enter the number of elements:")
n = int(input()) # input the number of elements

ourList = []
print("Enter the elements of the array:")
for i in range (n):
    ourList.append(int(input())) #inputting our array
print("Enter the number you are searching for: ")
needle = int(input())

pressenceCheck = False

for i in range(n):
    if ourList[i] == needle:
        pressenceCheck = True

if pressenceCheck == True:
    print("The number is in the array!")
else:
    print("Number is not in the array!")    

