#!/usr/bin/python
from copy import copy, deepcopy

def swap(matrix, i1, j1, i2, j2):
    buf = matrix[i1][j1]
    matrix[i1][j1] = matrix[i2][j2]
    matrix[i2][j2] = buf

# Rotate matrix on 90 degrees
def rotate_matrix(matrix, left = False):
    # result = deepcopy(matrix)
    result= matrix
    n = len(result)
    for i in range(n):
        for j in range(n):
            if left:
                result[n - 1 - j][i] = matrix[i][j]
            else:
                result[j][n - 1 - i] = matrix[i][j]

    return result

def left_rotation_coordinates(coords, n):
    return n - 1 - coords[1], coords[0]

def right_rotation_coordinates(coords, n):
    return coords[1], n - 1 - coords[0]

def rotate_four_points(matrix, pivot, n, coordinates_calculation_method):
    first_movement_coordinates = coordinates_calculation_method(pivot, n)
    second_movement_coordinates = coordinates_calculation_method(first_movement_coordinates, n)
    third_movement_coordinates = coordinates_calculation_method(second_movement_coordinates, n)
    tmp = matrix[first_movement_coordinates[0]][first_movement_coordinates[1]]
    matrix[first_movement_coordinates[0]][first_movement_coordinates[1]] = matrix[pivot[0]][pivot[1]]
    matrix[pivot[0]][pivot[1]] = matrix[third_movement_coordinates[0]][third_movement_coordinates[1]]
    matrix[third_movement_coordinates[0]][third_movement_coordinates[1]] = matrix[second_movement_coordinates[0]][second_movement_coordinates[1]]
    matrix[second_movement_coordinates[0]][second_movement_coordinates[1]] = tmp

# Rotate matrix on 90 degrees
def rotate_matrix_efficient(matrix, left = False):
    # result = deepcopy(matrix)
    result = matrix
    n = len(result)
    coordinates_calculation_method = right_rotation_coordinates
    if left:
        coordinates_calculation_method = left_rotation_coordinates
    for i in range(n//2):
        for j in range(n - 1 - i):
            rotate_four_points(result, (i, j), n, coordinates_calculation_method)

    return result