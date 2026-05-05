#!/usr/bin/env python3

i = 97
while i < 123:
    if chr(i) not in "eq":
        print(chr(i), end='')
    i += 1
print()