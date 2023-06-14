#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0] * len(row) for row in matrix]

    for idx in range(len(matrix)):
        for ridx in range(len(matrix[idx])):
            new_matrix[idx][ridx] = pow(matrix[idx][ridx], 2)
    return (new_matrix)
