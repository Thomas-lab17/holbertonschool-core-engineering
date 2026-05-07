#!/usr/bin/env python3

def uppercase(str):
    new_str = ""

    for c in str:
        if 97 <= ord(c) <= 122:
            new_str += chr(ord(c) - 32)
        else:
            new_str += c
    print("{}".format(new_str))
