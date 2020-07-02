# Studying the Fibonacci in depth

#Attempt 1

nums = int(input())

def fibonnaci(numVals):
    i = 0
    a = 0
    b = 1
    c = 0
    while i < numVals:
        print (c)
        c = a + b
        a = b
        b = c

        i += 1

fibonnaci(nums)

# Recursion Method
n = 0
d = 1

def fibrecurse(n):
    if n == 0:
        return n
    else:
        print(n+d)
        return fibrecurse(n = d)
