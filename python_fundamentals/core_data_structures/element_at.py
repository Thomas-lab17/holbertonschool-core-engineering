#!/usr/bin/env python3


def element_at(my_list, idx):
    """Retrieve an element from a list safely.

    Args:
        my_list: List of elements.
        idx: Index of the element to retrieve.

    Returns:
        The element at position idx, or None if idx is negative/out of range.
    """

    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
