#!/usr/bin/env python3
def pow(a, b):
    """Return a raised to the power of b using a loop.
    Assumes b is a non‑negative integer.
    """
    result = 1
    for _ in range(b):
        result *= a
    return result
