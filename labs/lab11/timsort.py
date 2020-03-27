"""CSC148 Lab 11: More on sorting

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains a mutating implementation of mergesort,
and a skeleton implementation of Timsort that you will work through
during this lab.
"""
from typing import Optional, List, Tuple


###############################################################################
# Introduction: mutating version of mergesort
###############################################################################
def mergesort2(lst: list,
               start: int = 0,
               end: Optional[int] = None) -> None:
    """Sort the items in lst[start:end] in non-decreasing order.

    Note: this is a *mutating, in-place* version of mergesort,
    meaning it does not return a new list, but instead sorts the input list.

    When we divide the list into halves, we don't create new lists for each
    half; instead, we simulate this by passing additional parameters (start
    and end) to represent the part of the list we're currently recursing on.
    """
    if end is None:
        end = len(lst)

    if start < end - 1:
        mid = (start + end) // 2
        mergesort2(lst, start, mid)
        mergesort2(lst, mid, end)
        _merge(lst, start, mid, end)


def _merge(lst: list, start: int, mid: int, end: int) -> None:
    """Sort the items in lst[start:end] in non-decreasing order.

    Precondition: lst[start:mid] and lst[mid:end] are sorted.
    """
    result = []
    left = start
    right = mid
    while left < mid and right < end:
        if lst[left] < lst[right]:
            result.append(lst[left])
            left += 1
        else:
            result.append(lst[right])
            right += 1

    # This replaces lst[start:end] with the correct sorted version.
    lst[start:end] = result + lst[left:mid] + lst[right:end]


###############################################################################
# Task 1: Finding runs
###############################################################################
def find_runs(lst: list) -> List[Tuple[int, int]]:
    """Return a list of tuples indexing the runs of lst.

    Precondition: lst is non-empty.

    >>> find_runs([1, 4, 7, 10, 2, 5, 3, -1])
    [(0, 4), (4, 6), (6, 7), (7, 8)]
    >>> find_runs([0, 1, 2, 3, 4, 5])
    [(0, 6)]
    >>> find_runs([10, 4, -2, 1])
    [(0, 1), (1, 2), (2, 4)]
    """
    runs = []
    break_indexes = []
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            break_indexes.append(i)
    if len(break_indexes) > 1 and break_indexes[0] != 0 and break_indexes[-1] != len(lst):
        break_indexes.insert(0, 0)
        break_indexes.append(len(lst))
    else:
        runs.append((0, len(lst)))
    for i in range(len(break_indexes) - 1):
        runs.append((break_indexes[i], break_indexes[i + 1]))
    return runs


###############################################################################
# Task 2: Merging runs
###############################################################################
def timsort(lst: list) -> None:
    """Sort <lst> in place.

    >>> lst = []
    >>> timsort(lst)
    >>> lst
    []
    >>> lst = [1]
    >>> timsort(lst)
    >>> lst
    [1]
    >>> lst = [1, 4, 7, 10, 2, 5, 3, -1]
    >>> timsort(lst)
    >>> lst
    [-1, 1, 2, 3, 4, 5, 7, 10]
    """
    runs = find_runs(lst)
    while len(runs) > 1:
        run1 = runs.pop()
        run2 = runs.pop()
        _merge(lst, run2[0], run2[1], run1[1])
        new_runs = find_runs(lst)
        for t in new_runs:
            runs.append(t)


###############################################################################
# Task 3: Descending runs
###############################################################################
def find_runs2(lst: list) -> List[Tuple[int, int]]:
    """Return a list of tuples indexing the runs of lst.

    Now, a run can be either ascending or descending!

    Precondition: lst is non-empty.

    First set of doctests, just for finding descending runs.
    >>> find_runs2([5, 4, 3, 2, 1])
    [(0, 5)]
    >>> find_runs2([1, 4, 7, 10, 2, 5, 3, -1])
    [(0, 4), (4, 6), (6, 8)]
    >>> find_runs2([0, 1, 2, 3, 4, 5])
    [(0, 6)]
    >>> find_runs2([10, 4, -2, 1])
    [(0, 3), (3, 4)]

    The second set of doctests, to check that descending runs are reversed.
    >>> lst1 = [5, 4, 3, 2, 1]
    >>> find_runs2(lst1)
    [(0, 5)]
    >>> lst1  # The entire run is reversed
    [1, 2, 3, 4, 5]
    >>> lst2 = [1, 4, 7, 10, 2, 5, 3, -1]
    >>> find_runs2(lst2)
    [(0, 4), (4, 6), (6, 8)]
    >>> lst2  # The -1 and 3 are switched
    [1, 4, 7, 10, 2, 5, -1, 3]
    """
    runs = []
    break_indexes = []
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            break_indexes.append(i)
    if len(break_indexes) > 1 and break_indexes[0] != 0 and break_indexes[-1] != len(lst):
        break_indexes.insert(0, 0)
        break_indexes.append(len(lst))
    else:
        runs.append((0, len(lst)))
    for i in range(len(break_indexes) - 1):
        runs.append((break_indexes[i], break_indexes[i + 1]))
    return runs


###############################################################################
# Task 4: Minimum run length
###############################################################################
MIN_RUN = 64


def find_runs3(lst: list) -> List[Tuple[int, int]]:
    """Same as find_runs2, but each run (except the last one)
    must be of length >= MIN_RUN.

    Precondition: lst is non-empty
    """
    runs = []
    break_indexes = []
    while len(runs) >= MIN_RUN:
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                break_indexes.append(i)
        if len(break_indexes) > 1 and break_indexes[0] != 0 and break_indexes[-1] != len(lst):
            break_indexes.insert(0, 0)
            break_indexes.append(len(lst))
        else:
            runs.append((0, len(lst)))
        for i in range(len(break_indexes) - 1):
            runs.append((break_indexes[i], break_indexes[i + 1]))
        return runs


def insertion_sort(lst: list, start: int, end: int) -> None:
    """Sort the items in lst[start:end] in non-decreasing order.
    """
    for i in range(start + 1, end):
        num = lst[i]
        left = start
        right = i
        while right - left > 1:
            mid = (left + right) // 2
            if num < lst[mid]:
                right = mid
            else:
                left = mid + 1

        # insert
        if lst[left] > num:
            lst[left + 1:i + 1] = lst[left:i]
            lst[left] = num
        else:
            lst[right + 1:i + 1] = lst[right:i]
            lst[right] = num


###############################################################################
# Task 5: Optimizing merge
###############################################################################
def _merge2(lst: list, start: int, mid: int, end: int) -> None:
    """Sort the items in lst[start:end] in non-decreasing order.

    Precondition: lst[start:mid] and lst[mid:end] are sorted.
    """
    len1 = mid - start + 1
    len2 = end - mid
    left = []
    right = []
    for i in range(0, len1):
        left.append(lst[start + i])
    for i in range(0, len2):
        right.append(lst[mid + 1 + i])
    index1 = 0
    index2 = 0
    begin = start
    while index1 < len1 and index2 < len2:
        if left[index1] <= right[index2]:
            lst[begin] = left[index1]
            index1 += 1
        else:
            lst[begin] = right[index2]
            index2 += 1
        begin += 1
    while index1 < len1:
        lst[begin] = left[index1]
        begin += 1
        index1 += 1
    while index2 < len2:
        lst[begin] = right[index2]
        begin += 1
        index2 += 1


###############################################################################
# Task 6: Limiting the 'runs' stack
###############################################################################
def timsort2(lst: list) -> None:
    """Sort the given list using the version of timsort from Task 6.
    """
    runs = find_runs3(lst)
    while len(runs) >= 3:
        a = runs.pop()
        b = runs.pop()
        c = runs.pop()
        if len(b) > len(c) and len(a) > len(b) + len(c):
            new_runs = find_runs3(lst)
            for t in new_runs:
                runs.append(t)
        elif len(b) <= len(c):
            _merge2(lst, c[0], c[1], b[1])
        else:
            _merge2(lst, c[0], a[0], a[1])


# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod()
