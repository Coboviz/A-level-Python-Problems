#write a recursive function which returns the greatest common divisor
#                                             highest  common factor
# hcf (24, 36) = 12
def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a%b)
    
print(hcf(78, 48))