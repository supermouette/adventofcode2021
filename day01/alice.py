import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    lines = f.readlines()
lines = [int(l) for l in lines]

# part A
cpt = 0
for i in range(1, len(lines)):
    if lines[i-1] < lines[i]:
        cpt += 1

print(cpt)

# part B
cpt = 0
for i in range(1, len(lines) - 2):
    if lines[i-1] + lines[i] + lines[i+1] < lines[i] + lines[i+1] + lines[i+2]:
        cpt += 1
print(cpt)


# generalisation

def countIncrease(array, n=3):
    cpt = 0
    for i in range(1, len(lines) - n + 1):
        if sum(array[i-1:i+n-1]) < sum(array[i:i+n]):
            cpt += 1
    return cpt

n = 125
plt.plot(list(range(1, n)), [countIncrease(lines, i) for i in range(1, n)])
plt.show()

plt.plot(list(range(len(lines))), lines, 'ro')
plt.show()
