# given a real number x and a non negative integer n, return x^n

def power(x, n):
    if (n == 0):
        return 1
    elif (n == 1):
        return x
    else:
        return x * power(x, n - 1)
    
print(power(2, 6))
print(power(2.14, 0))