#!/usr/bin/env python3
"""
Module defining a VerboseList class that extends Python's built-in list
and prints notifications on modifications.
"""


class VerboseList(list):
    """
    A list subclass that prints messages when modified.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification.

        Args:
            item: The item to be added.
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """
        Extend the list with elements from an iterable and print a
        notification.

        Args:
            iterable: An iterable containing items to add.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification.

        Args:
            item: The item to be removed.

        Raises:
            ValueError: If the item is not in the list.
        """
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item at the given index and print a
        notification.

        Args:
            index (int, optional): The index of the item to remove.
                Defaults to -1 (last item).

        Returns:
            The removed item.

        Raises:
            IndexError: If the list is empty or index is out of range.
        """
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


if __name__ == "__main__":
    """
    Test the VerboseList class.
    """
    v_list = VerboseList([1, 2, 3])

    v_list.append(4)
    v_list.extend([5, 6])
    v_list.remove(2)
    v_list.pop()
    v_list.pop(0)
