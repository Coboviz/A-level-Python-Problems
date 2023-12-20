# Write a recursive function which calculates nth term of the Fibonacci sequence.
# Fibonacci sequence is: 0 1 1 2 3 5 8 13 ... (nth term is equal to the sum of previous two)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range (150):
    print (fibonacci(i))