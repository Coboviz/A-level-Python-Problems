def fun2(x, y):
    if x == 0:
        return y
    else:
        return fun2(x - 1, x + y)
    
print(fun2(1, 3))
print(fun2(2, 7))
print(fun2(4, 6))
print(fun2(5, 10))
print(fun2(9, 13))

# 7 + 2 + 1
# 10 + 5 + 4 + 3 + 2 + 1
# 13 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1