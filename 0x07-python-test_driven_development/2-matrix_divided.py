#!/usr/bin/python3
"""creates a function that divides a matrix"""


def matrix_divided(matrix, div):
    """args
    arg1 : matrix
    arg2 : number to divide matrix by
    """
    new_matrix = []
    if type(matrix) not in [list]:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    for sub_list in matrix:
        for number in sub_list:
            if type(number) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
    list_len = len(matrix[0])

    for sub_list in matrix:
        if len(sub_list) != list_len:
            raise TypeError('Each row of the matrix must have the same size')
        else:
            list_len = len(sub_list)
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[eval("{:.2f}".format(num / div)) for num in row]
                  for row in matrix]
    return new_matrix
