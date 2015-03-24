def magic_square(matrix):
    magic_sum = sum(matrix[0])
    # rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    # columns
    for col in range(len(matrix[0])):
        sum_of_col = 0
        for row in matrix:
            sum_of_col += row[col]
        if sum_of_col != magic_sum:
            return False
    # diagonals
    main_diagonal_elements = [matrix[x][x] for x in range(len(matrix))]
    main_diagonal_sum = sum(main_diagonal_elements)
    other_diagonal_elements = [
        matrix[x][len(matrix) - x - 1] for x in range(len(matrix))]
    other_diagonal_sum = sum(other_diagonal_elements)
    if main_diagonal_sum != magic_sum or other_diagonal_sum != magic_sum:
        return False
    return True


matrix = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print(
    magic_square([
        [7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
