# Naive Algorithm

nums = int(input('please enter number'))
lst = []
vals = input().split()

def maximumPairwise(numbers, values):

    for i in range(numbers):
        if numbers != len(values):
            return print('Your values are less than the number you specified')
        else:
            lst.append(int(values[i]))

    lst.sort()
    maxNumber = lst.pop()
    maxNumber2 = lst.pop()

    product = maxNumber * maxNumber2

    return product

maximumPairwise(nums, vals)

'''
product = numbers * max(lst)
print(product)
'''


# Second Solution
'''
n = int(input())
a = [int(x) for x in input().split()]

print(a)


product = 0
for i in range(n):
    for j in range(i + 1, n):
        product = max(product, a[i] * a[j])

print(product)
'''
