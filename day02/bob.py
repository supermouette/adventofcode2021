import matplotlib.pyplot as plt
import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()
lines = [[l.split(" ")[0], int(l.split(" ")[1])] for l in lines]


def compute_position(array):
    pos = [0, 0]  # pos[horizontal, depth]
    history = [pos[:]]
    for a in array:
        if a[0] == "forward":
            pos[0] += a[1]
        elif a[0] == "down":
            pos[1] += a[1]
        elif a[0] == "up":
            pos[1] -= a[1]
        else:
            raise ValueError
        history.append(pos[:])
    return np.array(history)


positions = compute_position(lines)
print(positions[-1, :], positions[-1, 0]*positions[-1, 1])
plt.plot(positions[:, 0], positions[:, 1])
plt.show()


def compute_position_v2(array):
    pos = [0, 0, 0]  # pos[horizontal, depth, aim]
    history = [pos[:-1]]
    for a in array:
        if a[0] == "forward":
            pos[0] += a[1]
            pos[1] += a[1]*pos[2]
        elif a[0] == "down":
            pos[2] += a[1]
        elif a[0] == "up":
            pos[2] -= a[1]
        else:
            raise ValueError
        history.append(pos[:-1])
    return np.array(history)


positions = compute_position_v2(lines)
print(positions[-1, :], positions[-1, 0]*positions[-1, 1])
plt.plot(positions[:, 0], positions[:, 1])
plt.show()
