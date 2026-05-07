#!/usr/bin/env python3
def islower(c):
    alphabet = list(range(ord('a'), ord('z')))
    c = ord(c)
    if c in alphabet:
        return True
    else:
        return False
