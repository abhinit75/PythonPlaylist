"""
import numpy as np

n = int(input("n: "))  # rows
m = int(input("m: "))  # columns

arr = np.zeros((n, m))
print(arr)

for i in arr.flat:
    a = input()
    np.where(arr == 0, a, arr)

print(arr)
"""

