# Studying the Fibonacci in depth
'''
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
# returns the nth number

def fibrecurse(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibrecurse(n-2) + fibrecurse(n-1)

print(fibrecurse(nums))

'''
'''
Very inefficient
- fibonnaci(5) --> fibonnaci (4) --> onwards
- fibonacci (3) + fibonnaci(2) + fibonnaci(2) + fibonnaci(1)
- fibonnaci(2) + fibonnaci(1) + fobonacci(2) fibonnaci(2) + fibonnaci(1)
- finally - 1 + 1 + 1 + 1 + 1

'''


# Memoization
fibonacci_cache = {}

def fibonacci(n):
    #If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 101):
    print(n, ":", fibonacci(n))


# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
def memoize_factorial(f):
    memory = {}

    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


print(facto(5))