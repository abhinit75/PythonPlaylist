# Naive Algorithm (Attempt 1)

numOne = int(input("Please enter the first number"))
numTwo = int(input("Please enter the second number"))
gcdlst = []

def gcd(x, y):
    divlstx = []
    divlsty = []
    for i in range(1, x+1):
        if x % i == 0:
            divlstx.append(i)
        else:
            continue

    for j in range(1, y+1):
        if y % j == 0:
            divlsty.append(j)
        else:
            continue

    for num in divlstx:
        for vals in divlsty:
            if num == vals:
                gcdlst.append(num)
            else:
                continue

    return print(max(gcdlst))

gcd(numOne, numTwo)

# Attempt 2: Euclidean Algorithm

def euclideanAlgo(a, b):
    if a % b


