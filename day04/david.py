import numpy as np

# data
with open("input.txt", "r") as f:
    lines = f.readlines()
lines = [l.strip("\n") for l in lines]

numbers = lines[0].split(",")
numbers = [int(nb) for nb in numbers]
boards = [[]]
lines = lines[2:]

for line in lines:
    if len(line) == 0:
        boards.append([])

    else:
        boards[-1].append(line.split(" "))
        while "" in boards[-1][-1]:
            boards[-1][-1].remove("");
        boards[-1][-1] = [int(nb) for nb in boards[-1][-1]]


boards = np.array(boards)
binary_boards = np.full(boards.shape, False, dtype=bool)


binary_boards[boards == numbers[0]] = True


# utility
def check_victory(bin_boards, board_index):
    board = bin_boards[board_index]
    row_check = max([np.sum(board[irow, :]) for irow in range(board.shape[0])])
    col_check = max([np.sum(board[:, icol]) for icol in range(board.shape[1])])
    return row_check == board.shape[0] or col_check == board.shape[1]


def count_score(boards, bin_boards, board_index):
    board = boards[i]
    bin_board = bin_boards[i]
    board[bin_board] = 0
    return np.sum(board)


# find best (part 1)
for nb in numbers:
    binary_boards[boards == nb] = True
    for i in range(boards.shape[0]):
        if check_victory(binary_boards, i):
            print(count_score(boards, binary_boards, i)*nb)
            break
    else:
        continue
    break

# find worst (part 2)
has_won = set()
for nb in numbers:
    binary_boards[boards == nb] = True
    for i in range(boards.shape[0]):
        if check_victory(binary_boards, i):
            if i not in has_won:
                if len(has_won) != boards.shape[0]-1:
                    has_won.add(i)
                else:
                    print(count_score(boards, binary_boards, i) * nb)
                    break
    else:
        continue
    break
