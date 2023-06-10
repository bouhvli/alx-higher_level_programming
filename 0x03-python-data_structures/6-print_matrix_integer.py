#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("{}".format(matrix))
    else:
        for row in matrix:
            count = 0
            for element in row:
                print("{:d}".format(element), end='')
                count += 1
                if count != len(row):
                    print(end=' ')
            print()
