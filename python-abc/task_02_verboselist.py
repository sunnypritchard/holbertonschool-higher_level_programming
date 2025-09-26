#!/usr/bin/python3
"""Module define a class VerboseList that extends the built-in list."""


class VerboseList(list):
    """A class that extends the built-in list to add verbose output."""

    def append(self, item):
        """Append an item to the list and print a message."""

        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """Extend the list with items from an iterable and print a message."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """Remove an item from the list and print a message."""
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        """Remove and return an item at the given index and print a message."""
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


# Testing the VerboseList class:
if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)
