# Collatz Conjecture
'''
The challenge was to develop a program which performs the collatz conjecture
- Take two inputs, i & j
- i is the starting
Input
The input will consist of a series of pairs of integers i and j, one pair of integers per
line. All integers will be less than 1,000,000 and greater than 0.

Output
For each pair of input integers i and j, output i, j in the same order in which they
appeared in the input and then the maximum cycle length for integers between and
including i and j. These three numbers should be separated by one space, with all three
numbers on one line and with one line of output for each line of input.

'''

# Collatz Calculation Function
def Collatz(number):
    count = 0
    while number != 1:
        count = count + 1
        if number % 2 == 0:
            number = number // 2

        elif number % 2 != 0:
            number = (number * 3) + 1

    else:
        count = count + 1

    return count

# user input which defines range

i = int(input("i: "))
j = int(input("j: "))


a = []
for number in range(i, j + 1):
    a.append(Collatz(number))

cycle_length = 0

# values counter
for b in a:
    if cycle_length < b:
        cycle_length = b

print(i, j, cycle_length)

# Other Attempts
'''
i = int(input("i: "))
j = int(input("j: "))
n = 0

for a in range(i, j):
    while a != 1:
        if a % 2 == 0:
            a = i / 2

        elif a % 2 != 0:
            a = (a * 3) + 1

        print(a)

    else:
        break

print(i, j, n)
'''
'''
i = int(input("i: "))
j = int(input("j: "))

count = 0

for number in range(i, j):

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            count = count + 1

        else:
            number = (number * 3) + 1
            count = count + 1

        
print(count)
'''
'''

def Collatz(i, j):
    count = 0
    i = int(i)
    j = int(j)
    for number in range(i, j):
        while number != 1:
            if number % 2 == 0:
                number = number // 2
                count = count + 1

            elif number % 2 != 0:
                number = (number * 3) + 1
                count = count + 1

        else:
            count = count + 1
            return count


print(Collatz(1, 10))
'''

