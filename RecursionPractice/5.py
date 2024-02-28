# 12345 -> 10230450
def addZero(number, index, result):
    s = str(number)
    if index == len(s):
        return result
    if int(s[index]) % 2 == 1:
        result = result + s[index] + "0"
        return addZero(number, index + 1, result)
    else:
        result = result + s[index]
        return addZero(number, index + 1, result)
    
print(addZero(12345, 0, ""))
    