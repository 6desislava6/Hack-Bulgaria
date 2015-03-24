from sum_matrix import sum_matrix
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def depending_on_index(m, index_i, index_j):
    rows = len(m) - 1 
    cols = len(m[0]) - 1
    pos = 'middle'
    if index_i == 0:
        pos = 'up'
    if index_i == rows:
        pos = 'down'
    if index_j == 0:
        pos = 'left'
        if index_i == 0:
            pos = 'upleft'
        if index_i == rows:
            pos = 'downleft'
    if index_j == cols:
        pos = 'right'
        if index_i == 0:
            pos = 'upright'
        if index_i == rows:
            pos = 'downright'
    return pos


def matrix_bombing_plan(m):
    sum = sum_matrix(m)
    damages = {}
    for index_i in range(0, len(m)):
        for index_j in range(0, len(m[index_i])):
            damage = 0
            times_position = depending_on_index(m, index_i, index_j)
            position = times_position
            if position == 'middle':
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j + 1])
                damage += reduce (m[index_i][index_j],m[index_i][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i][index_j + 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j + 1])
            if position == 'up':
                damage += reduce (m[index_i][index_j],m[index_i][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i][index_j + 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j + 1])
            if position == 'down':
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j + 1])
                damage += reduce (m[index_i][index_j],m[index_i][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i][index_j + 1])
            if position == 'left':
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j + 1])
                damage += reduce (m[index_i][index_j],m[index_i][index_j + 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j + 1])
            if position == 'right':
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j])
            if position == 'upright':
                damage += reduce (m[index_i][index_j],m[index_i][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j])
            if position == 'downright':
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j - 1])
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i][index_j - 1])
            if position == 'upleft':
                damage += reduce (m[index_i][index_j],m[index_i][index_j + 1])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i + 1][index_j + 1])
            if position == 'downleft':
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j])
                damage += reduce (m[index_i][index_j],m[index_i - 1][index_j + 1])
                damage += reduce (m[index_i][index_j],m[index_i][index_j + 1])
            index = '(' + str(index_i) + ', ' + str(index_j) + ')'
            damages[index] = sum - damage
    print(damages)



def reduce (number, reducable_number):
    if reducable_number < number:
        return reducable_number
    else:
        return number

matrix_bombing_plan(m)