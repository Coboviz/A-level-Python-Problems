print("Enter the number of elements:")
n = int(input()) # input the number of elements

ourList = []
print("Enter the elements of the array:")
for i in range (n):
    ourList.append(int(input())) #inputting our array
print("Enter the number you are searching for: ")
needle = int(input())

ourList.sort()

found = False
searchFailed = False
left = 0
right = n - 1
while not found and not searchFailed:
    mid = (left + right) // 2 # 2 slashes for whole division
    if ourList[mid] == needle:
        found = True
    elif left >= right:
        searchFailed = True
    elif ourList[mid] > needle:
        right = mid - 1
    else:
        left = mid + 1

if found == True:
    print(mid) # printing the index of the element
else:
    print("not there")