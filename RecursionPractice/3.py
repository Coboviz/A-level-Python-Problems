# 12 -> 110
# 15 -> 120
# 27 -> 1000
# 98 -> 10122

def base3Rec(n):
    if n == 0:
        return ""
    else:
        return base3Rec(n // 3) + str(n % 3)
    
print(base3Rec(12))
print(base3Rec(137))