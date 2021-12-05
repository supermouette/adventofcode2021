import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

matrix = np.array([[int(c) for c in line.strip("\n")] for line in lines])

gamma_digit = [1 if np.average(matrix[:, digit]) > 0.5 else 0 for digit in range(matrix.shape[1])]
epsilon_digit = [1-g for g in gamma_digit]


def binary_list_to_decimal(bin_list):
    decimal = 0
    for i in range(len(bin_list)):
        decimal += bin_list[i] * 2 ** (len(bin_list) - 1- i)
    return decimal


power_consumption = binary_list_to_decimal(gamma_digit)*binary_list_to_decimal(epsilon_digit)
print(power_consumption)

# part 2


def oxygen(mat, digit):
    if mat.shape[0] == 1:
        return binary_list_to_decimal(list(mat[0, :]))
    else:
        most_digit = 1 if np.average([d for d in mat[:, digit]]) >= 0.5 else 0
        if most_digit == 1:
            bin_mat = mat[:, digit] > 0.5
        else:
            bin_mat = mat[:, digit] < 0.5
        return oxygen(mat[bin_mat, :], digit+1)


def co2(mat, digit):
    # I should refactor to have only one function "gaz"
    if mat.shape[0] == 1:
        return binary_list_to_decimal(list(mat[0, :]))
    else:
        most_digit = 0 if np.average([d for d in mat[:, digit]]) >= 0.5 else 1
        if most_digit == 1:
            bin_mat = mat[:, digit] > 0.5
        else:
            bin_mat = mat[:, digit] < 0.5
        return co2(mat[bin_mat, :], digit+1)


o = oxygen(matrix, 0)
c = co2(matrix, 0)
print(o,c, o*c)
