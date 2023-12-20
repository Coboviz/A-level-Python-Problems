def factoriel(n):
    if n == 1:
        return 1
    else:
        return n * factoriel(n-1)
    
print(factoriel(5))


# factoriel(5) = 5 * factoriel(4) = 5 * (4 * factoriel(3)) = 
# 5 * (4 * (3 * factoriel(2))) = 5 * (4 * (3 * (2 * factoriel(1)))) = 5 * 4 * 3 * 2 * 1 = 120

