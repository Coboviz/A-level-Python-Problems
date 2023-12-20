# write a recursive function to count the number of digits in a number

def countDigits(n):
    if (n < 10):
        return 1
    else:
        return 1 + countDigits(n//10)

print(countDigits(12345))
print(countDigits(0))