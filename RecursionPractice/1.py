def fun1(n):
    if n == 1:
        return 0
    else:
        return 1 + fun1(n // 2)
    
print(fun1(15))
print(fun1(321))
print(fun1(10))
print(fun1(9))
print(fun1(8))
print(fun1(17))