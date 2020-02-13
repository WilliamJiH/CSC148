"""Lab 6: Recursion

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a few nested list functions for you to practice recursion
"""
from typing import Union, List


def greater_than_all(obj: Union[int, List], n: int) -> bool:
    """Return True iff there is no int in <obj> that is larger than or
    equal to <n> (or, equivalently, <n> is greater than all ints in <obj>).

    >>> greater_than_all(10, 3)
    False
    >>> greater_than_all([1, 2, [1, 2], 4], 10)
    True
    >>> greater_than_all([], 0)
    True
    """
    if isinstance(obj, int):
        if n <= obj:
            return False
        return True
    else:
        res = []
        for sub in obj:
            res.append(greater_than_all(sub, n))
        return all(e is True for e in res)


def add_n(obj: Union[int, List], n: int) -> Union[int, List]:
    """Return a new nested list where <n> is added to every item in <obj>.

    >>> add_n(10, 3)
    13
    >>> add_n([1, 2, [1, 2], 4], 10)
    [11, 12, [11, 12], 14]
    """
    if not isinstance(obj, list):
        return n + obj
    else:
        res = []
        for sub in obj:
            res.append(add_n(sub, n))
        return res


def nested_list_equal(obj1: Union[int, List], obj2: Union[int, List]) -> bool:
    """Return whether two nested lists are equal, i.e., have the same value.

    Note: order matters.
    You should only use == in the base case. Do NOT use it to compare
    otherwise (as that defeats the purpose of this exercise)!

    >>> nested_list_equal(17, [1, 2, 3])
    False
    >>> nested_list_equal([1, 2, [1, 2], 4], [1, 2, [1, 2], 4])
    True
    >>> nested_list_equal([1, 2, [1, 2], 4], [4, 2, [2, 1], 3])
    False
    """
    if isinstance(obj1, int) and isinstance(obj2, int):
        if obj1 != obj2:
            return False
        return True
    elif isinstance(obj1, list) and isinstance(obj2, list) and len(obj1) == len(
            obj2):
        res = []
        for i in range(len(obj1)):
            res.append(nested_list_equal(obj1[i], obj2[i]))
        return all(e is True for e in res)
    return False


def duplicate(obj: Union[int, List]) -> Union[int, List]:
    """Return a new nested list with all numbers in <obj> duplicated.

    Each integer in <obj> should appear twice *consecutively* in the
    output nested list. The nesting structure is the same as the input,
    only with some new numbers added. See doctest examples for details.

    If <obj> is an int, return a list containing two copies of it.

    >>> duplicate(1)
    [1, 1]
    >>> duplicate([])
    []
    >>> duplicate([1, 2])
    [1, 1, 2, 2]
    >>> duplicate([1, [2, 3]])  # NOT [1, 1, [2, 2, 3, 3], [2, 2, 3, 3]]
    [1, 1, [2, 2, 3, 3]]
    """
    res = []
    if isinstance(obj, list) and len(obj) == 0:
        return res
    elif isinstance(obj, int):
        res.append(obj)
        res.append(obj)
    else:
        if isinstance(obj, list):
            for i in range(len(obj)):
                if isinstance(obj[i], int):
                    res.append(obj[i])
                    res.append(obj[i])
                elif isinstance(obj[i], list):
                    temp = duplicate(obj[i])
                    res.append(temp)
                continue
    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # import python_ta
    # python_ta.check_all()
