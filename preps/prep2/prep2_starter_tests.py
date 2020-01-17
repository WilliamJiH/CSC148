"""Prep 2 Synthesize Sample Tests

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains sample tests for Prep 2.
Complete the TODO in this file.

We suggest you also add your own tests to practice writing tests and
to be confident your code is correct.

When writing a test case, make sure you create a new function, with its
name starting with "test_". For example:

def test_my_test_case():
    # Your test here
"""
from hypothesis import given
from hypothesis.strategies import integers

from prep2 import Spinner


def test_buggy_consecutive_spins() -> None:
    """Test consecutive spins of your Spinner class.
    This test case has a bug in it."""

    # TODO: There is a bug in this test case -- find it and fix it.
    #       In its original state, this test case should NOT pass if
    #       your Spinner is implemented correctly!
    #       Do NOT change or remove any of the lines labelled with
    #       "Do not change this line".

    s = Spinner(6)  # Do not change this line
    s.spin(2)  # Do not change this line
    expected_value1 = 2
    assert s.position == expected_value1  # Do not change this line
    s.spin(2)  # Do not change this line
    expected_value2 = 4
    assert s.position == expected_value2  # Do not change this line


# === Sample test cases below ===
# Use the below test cases as an example for writing your own test cases,
# and as a start to testing your prep2.py code.

# WARNING: THIS IS CURRENTLY AN EXTREMELY INCOMPLETE SET OF TESTS!
# We will test your code on a much more thorough set of tests!

# For more information on hypothesis (one of the testing libraries we're using),
# please see
# <https://www.teach.cs.toronto.edu/~csc148h/fall/notes/testing/hypothesis.html>

# This is a hypothesis test; it generates a random integer to use as input,
# so that we don't need to hard-code a specific number of slots in the test.
@given(slots=integers(min_value=1))
def test_new_spinner_position(slots: int) -> None:
    """Test that the position of a new spinner is always 0."""
    spinner = Spinner(slots)
    assert spinner.position == 0


@given(force=integers(min_value=1))
def test_normal_spin(force: int) -> None:
    """Test that the position is inside the range during normal spin"""
    spinner = Spinner(100)
    cnt = []
    for i in range(1000):
        spinner.spin(force)
        cnt.append(spinner.position)
    cnt = list(filter(lambda x: x not in range(0, 100), cnt))
    assert cnt == [], "The position should never greater than 99."


def test_random_spin() -> None:
    """Test that the position is inside the range during spin randomly."""
    spinner = Spinner(100)
    cnt = []
    for i in range(1000):
        spinner.spin_randomly()
        cnt.append(spinner.position)
    cnt = list(filter(lambda x: x not in range(0, 100), cnt))
    assert cnt == [], "You should never spin out of range."


def test_doctest() -> None:
    """Test the given doctest in the Spinner class docstring."""
    spinner = Spinner(8)

    spinner.spin(4)
    assert spinner.position == 4

    spinner.spin(2)
    assert spinner.position == 6

    spinner.spin(2)
    assert spinner.position == 0


if __name__ == '__main__':
    import pytest

    pytest.main(['prep2_starter_tests.py'])
