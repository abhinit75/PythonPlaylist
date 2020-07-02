# Recursive method
nums = int(input("Enter number"))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

product = factorial(nums)

print(product)

#Tail-call optimization
aval = 1
def ftr(n, a):
    if n == 0 or n == 1:
        return a
    else:
        return ftr(n-1, n*a)

print(ftr(nums, aval))

