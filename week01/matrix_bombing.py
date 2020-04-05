import copy
import numpy as np


def matrix_bombing_plan(m):

    row = len(m)
    col = len(m[0])
    keys = [(x, y) for x in range(0, row) for y in range(0, col)]
    tuple_of_positions = tuple(keys)
    dic = {}

    for t in tuple_of_positions:
        new_m = copy.deepcopy(m)

        if t[0] + 1 < row:
            if new_m[t[0] + 1][t[1]] - new_m[t[0]][t[1]] > 0:
                new_m[t[0] + 1][t[1]] -= new_m[t[0]][t[1]]
            else:
                new_m[t[0] + 1][t[1]] = 0
        if t[0] - 1 >= 0:
            if new_m[t[0] - 1][t[1]] - new_m[t[0]][t[1]] > 0:
                new_m[t[0] - 1][t[1]] -= new_m[t[0]][t[1]]
            else:
                new_m[t[0] - 1][t[1]] = 0
        if t[1] + 1 < col:
            if new_m[t[0]][t[1] + 1] - new_m[t[0]][t[1]] > 0:
                new_m[t[0]][t[1] + 1] -= new_m[t[0]][t[1]]
            else:
                new_m[t[0]][t[1] + 1] = 0
        if t[1] - 1 >= 0:
            if new_m[t[0]][t[1] - 1] - new_m[t[0]][t[1]] > 0:
                new_m[t[0]][t[1] - 1] -= new_m[t[0]][t[1]]
            else:
                new_m[t[0]][t[1] - 1] = 0
        if t[0] - 1 >= 0 and t[1] - 1 >= 0:
            if new_m[t[0] - 1][t[1] - 1] - new_m[t[0]][t[1]] > 0:
                new_m[t[0] - 1][t[1] - 1] -= new_m[t[0]][t[1]]
            else:
                new_m[t[0] - 1][t[1] - 1] = 0
        if t[0] + 1 < row and t[1] + 1 < col:
            if new_m[t[0] + 1][t[1] + 1] - new_m[t[0]][t[1]] > 0:
                new_m[t[0] + 1][t[1] + 1] -= new_m[t[0]][t[1]]
            else:
                new_m[t[0] + 1][t[1] + 1] = 0
        if t[0] - 1 >= 0 and t[1] + 1 < col:
            if new_m[t[0] - 1][t[1] + 1] - new_m[t[0]][t[1]] > 0:
                new_m[t[0] - 1][t[1] + 1] -= new_m[t[0]][t[1]]
            else:
                new_m[t[0] - 1][t[1] + 1] = 0
        if t[0] + 1 < row and t[1] - 1 >= 0:
            if new_m[t[0] + 1][t[1] - 1] - new_m[t[0]][t[1]] > 0:
                new_m[t[0] + 1][t[1] - 1] -= new_m[t[0]][t[1]]
            else:
                new_m[t[0] + 1][t[1] - 1] = 0
        dic[t] = np.sum(new_m)
    return dic


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(matrix_bombing_plan(m))


if __name__ == '__main__':
    main()
