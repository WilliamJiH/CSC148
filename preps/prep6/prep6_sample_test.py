"""CSC148 Prep 6: Recursion

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: David Liu and Diane Horton

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 David Liu and Diane Horton

=== Module description ===
This module contains sample tests for Prep 6.

WARNING: THIS IS AN EXTREMELY INCOMPLETE SET OF TESTS!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<https://www.teach.cs.toronto.edu/~csc148h/winter/notes/testing/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""
from prep6 import num_positives, nested_max, max_length


def test_num_positives_doctest_example() -> None:
    """Test num_positive on one of the given doctest examples."""
    assert num_positives([1, -2, [-10, 2, [3], 4, -5], 4]) == 5
    

def test_num_positives_empty_list() -> None:
    """Test num_positives on am empty list."""
    assert num_positives([]) == 0


def test_nested_max_doctest_example() -> None:
    """Test nested_max on one of the given doctest examples."""
    assert nested_max([1, 2, [1, 2, [3], 4, 5], 4]) == 5


def test_max_length_doctest_example() -> None:
    """Test nested_max on one of the given doctest examples."""
    assert max_length([1, 2, [1, 2], 4]) == 4


if __name__ == '__main__':
    import pytest
    pytest.main(['prep6_sample_test.py'])
