# Problem 1 of Project Euler

def multiplesof3or5(x=int(input())):
    nums = []
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            nums.append(i)
    Tsum = 0
    for number in nums:
        Tsum += number
    print(Tsum)

multiplesof3or5()