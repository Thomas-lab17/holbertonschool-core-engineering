#!/usr/bin/env python3
alphabet = list(range(97, 123))
alphabt = ""

for ascii in alphabet:
    if ascii != 101 and ascii != 113:
        letter = chr(ascii)
        alphabt += letter

print("{}".format(alphabt), end="")
