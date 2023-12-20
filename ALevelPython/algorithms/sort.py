list = [1, 2, -45, 692, 214, 634, 10000]

def sorting(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

sortedList = sorting(list)
print(sortedList)