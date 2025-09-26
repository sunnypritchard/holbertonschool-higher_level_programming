#!/usr/bin/python3
"""
This module defines a CountedIterator class that wraps around any iterable,
and counts the number of items retrieved.
"""


class CountedIterator:
    """
    A class that wraps around an iterable and counts the number of items
    retrieved.
    """

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item from the iterator and increment the count."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """Return the number of items retrieved so far."""
        return self.count


# ---------- Testing ----------
if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(
                f"Got {item}, total {counted_iter.get_count()} items iterated."
            )
    except StopIteration:
        print("No more items.")
