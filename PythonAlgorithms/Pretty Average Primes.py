#Pretty Average Primes
'''
Input Specification
The first line of input is the number 𝑇 (1≤𝑇≤1000), which is the number of test cases. Each of the next 𝑇 lines contain one integer 𝑁𝑖 (4≤𝑁𝑖≤1000000,1≤𝑖≤𝑇).
For 6 of the available 15 marks, all 𝑁𝑖<1000.

Output Specification
The output will consist of 𝑇 lines. The 𝑖𝑡ℎ line of output will contain two integers, 𝐴𝑖 and 𝐵𝑖, separated by one space. It should be the case that 𝑁𝑖=𝐴𝑖+𝐵𝑖2 and that 𝐴𝑖 and 𝐵𝑖 are prime numbers.
If there are more than one possible 𝐴𝑖 and 𝐵𝑖 for a particular 𝑁𝑖, output any such pair. The order of the pair 𝐴𝑖 and 𝐵𝑖 does not matter.
It will be the case that there will always be at least one set of values 𝐴𝑖 and 𝐵𝑖 for any given 𝑁𝑖.
'''

import random

while True:
    try:
        T = int(input("Please enter number of input lines"))
        if 1 <= T <= 1000 is not False:
            break
    except:
        print("Please enter a valid value")
        continue
n = 0
a = 0
b = 0
l = []

while n <= (T - 1):
    number = int(input(''))
    if 4 <= number <= 1000000 is not False:
        l.append(number)
        n += 1
    else:
        print('Please enter value between 4 and 1000000')

'''
for i in l:  # number in list
    d = i*2  # double input value
    while True:
        if (a % 2) == 0 and (b % 2) == 0:
            a += 1
            b += 1

        else:
            if (a + b) == d:
                print(a, b)
            break
'''
prime = []
for i in range(3, 50):
    if i % 2 != 0:
        prime.append(i)

for i in l:
    d = i * 2
    for n in prime:
        while a + b != d:
            a = random.choice(prime)
            b = random.choice(prime)
        else:
            print(a)
            print(b)
            break
