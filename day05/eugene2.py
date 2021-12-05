with open("input.txt", "r") as f:
    lines = f.readlines()
lines = [[[int(number)for number in part.split(",")] for part in line.strip('\n').split(" -> ")] for line in lines]

# part1
points = {}


def add_points(p, i, j):
    name = str(i)+'-'+str(j)
    if name in p:
        p[name] += 1
    else:
        p[name] = 1


for line in lines:
    if line[0][0] == line[1][0]:
        if line[0][1] < line[1][1]:
            for j in range(line[0][1], line[1][1]+1):
                add_points(points, line[0][0], j)
        else:
            for j in range(line[1][1], line[0][1]+1):
                add_points(points, line[0][0], j)
    elif line[0][1] == line[1][1]:
        if line[0][0] < line[1][0]:
            for i in range(line[0][0], line[1][0]+1):
                add_points(points, i, line[0][1])
        else:
            for i in range(line[1][0], line[0][0]+1):
                add_points(points, i, line[0][1])
    else:  # diagonals
        i = line[0][0]
        j = line[0][1]
        if line[0][0] < line[1][0]:
            i_next = 1
        else:
            i_next = -1
        if line[0][1] < line[1][1]:
            j_next = 1
        else:
            j_next = -1
        while i != line[1][0]:
            add_points(points, i, j)
            i += i_next
            j += j_next
        add_points(points, line[1][0], line[1][1])


cpt = 0
for key in points.keys():
    if points[key] > 1:
        cpt += 1
print(cpt)
