#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_matrix in matrix:
        sub_matrix_len = len(sub_matrix)
        index = 0
        while sub_matrix_len > 0:
            print("{:d}".format(sub_matrix[index]), end=" ")
            index += 1
            sub_matrix_len -= 1

        print("")
