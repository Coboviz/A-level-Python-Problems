# write a recursive binary search
# return the index if found if not return -1

def binarySearch(array, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if (array[mid] == target):
            return mid
        elif array[mid] < target:
            return binarySearch(array, target, mid + 1, high)
        else:
            return binarySearch(array, target, low, mid - 1)
    else:
        return -1






array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binarySearch(array, 5, 0, 9))
print(binarySearch(array, 6, 0, 9))
print(binarySearch(array, 19, 0, 9))
print(binarySearch(array, 24, 0, 9))
print(binarySearch(array, -1, 0, 9))