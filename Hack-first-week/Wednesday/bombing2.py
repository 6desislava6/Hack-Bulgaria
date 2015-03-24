from sum_matrix import sum_matrix
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def reduce(number, reducable_number):
    if reducable_number < number:
        return reducable_number
    else:
        return number


def corners(m):
    damages = []
    # corners
    # top-left
    damages.append(
        reduce(m[0][0], m[0][1]) + reduce(m[0][0], m[1][0]) + reduce(m[0][0], m[1][1]))
    # bottom-left
    damages.append(reduce(
        m[-1][0], m[-2][1]) + reduce(m[-1][0], m[-2][0]) + reduce(m[-1][0], m[-1][1]))
    # top-right
    damages.append(reduce(
        m[0][-1], m[0][-2]) + reduce(m[0][-1], m[1][-1]) + reduce(m[0][-1], m[1][-2]))
    # bottom-right
    damages.append(reduce(
        m[-1][-1], m[-1][-2]) + reduce(m[-1][-1], m[-2][-1]) + reduce(m[-1][-1], m[-2][-2]))
    return damages


def up_side(m, i):
    damage = 0
    # up side:
    damage += reduce(m[0][i], m[0][i - 1]) + reduce(m[0][i], m[0][i + 1])
    damage += reduce(m[0][i], m[1][i - 1]) + \
        reduce(m[0][i], m[1][i]) + reduce(m[0][i], m[0][i + 1])
    return damage


def down_side(m, i):
    damage = 0
    # down side:
    damage += reduce(m[-1][i], m[-1][i - 1]) + reduce(m[-1][i], m[-1][i + 1])
    damage += reduce(m[-1][i], m[-2][i - 1]) + \
        reduce(m[-1][i], m[-2][i]) + reduce(m[-1][i], m[-2][i + 1])
    return damage


def left_side(m, i):
    damage = 0
    # left side:
    damage += reduce(m[i][0], m[i - 1][0]) + \
        reduce(m[i][0], m[i - 1][1]) + reduce(m[i][0], m[i][1])
    damage += reduce(m[i][0], m[i + 1][0]) + reduce(m[i][0], m[i + 1][1])
    return damage


def right_side(m, i):
    damage = 0
    # right side:
    damage += reduce(m[i][-1], m[i - 1][-2]) + reduce(m[i]
                                                    [-1], m[i - 1][-1]) + reduce(m[i][-i - 1], m[i][-2])
    damage += reduce(m[i][-1], m[i + 1][-2]) + reduce(m[i][-1], m[i + 1][-1])
    return damage


def middle(m, index_i, index_j):
    damage = 0
    damage += reduce(m[index_i][index_j], m[index_i - 1][index_j - 1])
    damage += reduce(m[index_i][index_j], m[index_i - 1][index_j])
    damage += reduce(m[index_i][index_j], m[index_i - 1][index_j + 1])
    damage += reduce(m[index_i][index_j], m[index_i][index_j - 1])
    damage += reduce(m[index_i][index_j], m[index_i][index_j + 1])
    damage += reduce(m[index_i][index_j], m[index_i + 1][index_j - 1])
    damage += reduce(m[index_i][index_j], m[index_i + 1][index_j])
    damage += reduce(m[index_i][index_j], m[index_i + 1][index_j + 1])
    return damage


def positions_as_tuples(m):
    rows = len(m)
    cols = len(m[0])
    positions = ()
    for i in range(0, rows):
        for j in range(0, cols):
            positions += ((i, j), )
    return positions


def matrix_bombing_plan(m):
    sum = sum_matrix(m)
    rows = len(m)
    cols = len(m[0])
    damages = {}
    positions = positions_as_tuples(m)
    corners_damages = corners(m)

    # corners
    damages[positions[0]] = sum - corners_damages[0]
    damages[positions[(rows - 1) * cols]] = sum - corners_damages[1]
    damages[positions[cols - 1]] = sum - corners_damages[2]
    damages[positions[rows * cols - 1]] = sum - corners_damages[3]

    # up and down
    for i in range(1, cols - 1):
        damages[positions[i]] = sum - up_side(m, i)
        damages[positions[i + (rows - 1) * cols]] = sum - down_side(m, i)

    # left and right
    for i in range(1, rows - 1):
        damages[positions[i * cols]] = sum - left_side(m, i)
        damages[positions[i * cols + (cols - 1)]] = sum - right_side(m, i)

    # middle ones
    for i in range(1, cols - 1):
        for j in range(1, rows - 1):
            damages[positions[i * cols + j]] = sum - middle(m, i, j)

    print(damages)

matrix_bombing_plan(m)
