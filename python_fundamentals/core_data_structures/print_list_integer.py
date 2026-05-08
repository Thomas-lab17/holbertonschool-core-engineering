#!/usr/bin/env python3

def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line."""

    for value in my_list:
        print("{:d}".format(value))
