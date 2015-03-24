def sum_matrix(matrix):
    sum = 0
    for row in matrix:
        for num in row:
            sum += num
    return sum