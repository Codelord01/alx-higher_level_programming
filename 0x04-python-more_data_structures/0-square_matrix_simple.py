#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []

    for sub_matrix in matrix:
        new_list = list(map(lambda x: x**2, sub_matrix))
        new_matrix.append(new_list)
    return new_matrix
