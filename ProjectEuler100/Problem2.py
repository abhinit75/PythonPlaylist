# Project Euler 2

a = 1
b = 0
c=  0
i = 0
total = 0
sum = []

while True:
    if c >= 4000000:
        break
    b = a
    a = c
    c = a+b
    if c%2 ==0:
        sum.append(c)

for i in sum:
    total += i

print(total)

