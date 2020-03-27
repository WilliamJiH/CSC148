"""
=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Quiz #11: Sorting ===
Define a function remove_duplicates, which takes a sorted list, and returns a new list with the same items as the
original, but without duplicates. Note that this function does not mutate the original list.

Take advantage of the fact that the input list is sorted! Your algorithm should run in time linear in the length of the
list.
"""
from typing import List


def remove_duplicates(lst: List) -> List:
    """Return a sorted list containing the same values as <lst>, but without duplicates.

    Precondition: <lst> is sorted.

    >>> remove_duplicates([1, 2, 2, 2, 3, 10, 10, 20])
    [1, 2, 3, 10, 20]
    """
    s = set()
    func = s.add
    return [item for item in lst if not (item in s or func(item))]
