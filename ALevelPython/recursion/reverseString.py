# write a recursive function which reverses the string sent as a parameter

# BrookHill -> lliHkoorB

def reverseString(s):
    if len(s) == 1: # checking if it's an empty string
        return s[0]
    else:
        return s[-1] + reverseString(s[:-1])



print(reverseString("BrookHill"))