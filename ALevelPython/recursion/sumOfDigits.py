# Write a recursive function which returns sum of digits of a positive integer

# function(1489) = 22

def sumOfDigits(n):
    if n < 10:
        return n
    else:
        return n%10 + sumOfDigits(n//10) 
    
print(sumOfDigits(1489))