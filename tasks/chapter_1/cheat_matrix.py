#!/usr/bin/python

# Cheat maatrix columns and lines if some element is 0
def cheat_matrix(matrix):
    rows = [False] * len(matrix)
    columns = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows[i] = True
                columns[j] = True

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if rows[i] or columns[j]:
                matrix[i][j] = 0

    return matrix