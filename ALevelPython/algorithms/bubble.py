def bubbleSort(list):
    numberOfElements = len(list) # to get the number of elements
    for i in range (numberOfElements):
        for j in range (numberOfElements - i - 1):
            if list[j+1] < list[j]:
                #list[i], list[j] = list[j], list[i]
                swap = list[j+1]
                list[j+1] = list[j]
                list[j] = swap
        
    return list

list = [64 , 7 , 11, 2, -3, 9, 55, 0, 156]

sortedList = bubbleSort(list)

print(sortedList)
        