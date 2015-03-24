from copy import deepcopy


def sum_matrix(m):
    return sum(map(sum, m))


def bomb_da_shet(m, pos):
    tmp = deepcopy(m)
    for row in range(len(tmp)):
        for col in range(len(tmp[0])):
            if (abs(row - pos[0]) <= 1 and abs(col - pos[1]) <= 1
                    and (row != pos[0] or col != pos[1])):
                if tmp[row][col] - tmp[pos[0]][pos[1]] < 0:
                    tmp[row][col] = 0
                else:
                    tmp[row][col] -= tmp[pos[0]][pos[1]]
    return tmp


def matrix_bombing_plan(m):
    lst = [(x, y) for x in range(len(m)) for y in range(len(m[0]))]
    dct = {tpl: sum_matrix(bomb_da_shet(m, tpl)) for tpl in lst}
    min_elem = min([x for x in dct.values()])
    min_dict = {x: min_elem for x in dct.keys() if dct[x] == min_elem}
    print(min_dict)
    return min_dict


def reps(input_items):
    return [x for x in input_items if input_items.count(x) != 1]


def matrix_bombing_plan2(m):
    a = {}
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            p = []
            for k in [-1, 1]:
                for l in [-1, 1]:
                    n = deepcopy(m)
                    if i + k >= 0 and i + k < len(n) and j + l >= 0 and j + l < len(n[i]):
                        n[i + k][j] = max(0, n[i + k][j] - n[i][j])
                        n[i][j + l] = max(0, n[i][j + l] - n[i][j])
                        n[i + k][j + l] = max(0, n[i + k][j + l] - n[i][j])
                    p += [n]

            q = deepcopy(m)
            for g in range(0, len(q)):
                for h in range(0, len(q[g])):
                    q[g][h] = min(
                        p[0][g][h], p[1][g][h], p[2][g][h], p[3][g][h])

            a[(i, j)] = sum_matrix(q)
    return a

if __name__ == '__main__':
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix_bombing_plan(m))
