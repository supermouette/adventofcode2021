import matplotlib.pyplot as plt
import numpy as np
from math import e

with open("input.txt", "r") as f:
    line = f.readline()

fishes = [int(fish) for fish in line.split(",")]
lens = []

for day in range(80):
    fish_len = len(fishes)
    lens.append(fish_len)
    for i in range(fish_len):
        fishes[i] -= 1
        if fishes[i] == -1:
            fishes[i] = 6
            fishes.append(8)

print(len(fishes))

# part 2 does't work T_T
"""
x = np.array(list(range(len(lens))) + [80])
y = np.array(lens + [len(fishes)])
print(x[-1], y[-1])
array = np.polyfit(x, np.log(y), 1)

y256 = e**array[1] * e**(array[0]*256)
# 255 : 1 523 167 249 168
# 256 : 1 662 107 375 259
print(y256)

plt.plot(list(range(len(lens))), lens)
plt.plot(x, [e**array[1] * e**(array[0]*y) for y in x])
plt.show()
"""

# a frind helped me T_T
mat = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.float64)

s = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=np.float64)

y = s - 1
fishes = [int(fish) for fish in line.split(",")]
for f in fishes:
    y[f] += 1

print(np.matmul(np.matmul(s, np.linalg.matrix_power(mat, 80)), y))
print(np.matmul(np.matmul(s, np.linalg.matrix_power(mat, 256)), y))

