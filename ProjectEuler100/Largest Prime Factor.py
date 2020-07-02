# Find largest prime factor of 600851475143
# Largest Prime Factor (Problem 3)

number = 600851475143
lst = []

i = 2

while i*i < number:
    while number%i == 0:
        number = number//i
    i = i+1

print(number)

# Other Attempts

'''
for i in range(1, number + 1):
    if number % i == 0:
        print(i)


for i in range(number):
    if i % 2 == 0:
        if i % 3 == 0:
            continue

    else:
        if number // i is True:
               lst.append(i)
               break

print(lst)
'''
'''


def factors(number):
    result = []
    i = 1

    while i * i <= number:
        if i%2 !=0 and i%3 !=0 and i%5 != 0 and i%7 != 0:
            if number % i == 0:
                result.append(i)
                if number // i != number:
                    result.append(number // i)
    i += 1

    return result

print(factors())
'''

