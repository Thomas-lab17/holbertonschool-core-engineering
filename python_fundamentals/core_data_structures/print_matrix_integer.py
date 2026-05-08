#!/usr/bin/env python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, value in enumerate(row):
            end = " " if idx < len(row) - 1 else ""
            print("{:d}".format(value), end=end)
        print()
