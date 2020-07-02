nums = int(input())
lst = []
vals = input().split()

def maximumPairwise(numbers, values):

    for i in range(numbers):
        if numbers != len(values):
            return
        else:
            lst.append(int(values[i]))

    lst.sort()
    maxNumber = lst.pop()
    maxNumber2 = lst.pop()

    product = maxNumber * maxNumber2

    return print(product)

maximumPairwise(nums, vals)