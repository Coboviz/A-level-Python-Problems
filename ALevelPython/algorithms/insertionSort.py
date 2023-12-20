def insertionSort(list):
    numberOfElements = len(list)
    for i in range (1, numberOfElements):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

list = [64 , 7 , 11, 2, -3, 9, 55, 0, 156]

sortedList = insertionSort(list)

print(sortedList)

