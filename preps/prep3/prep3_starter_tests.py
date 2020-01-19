"""CSC148 Prep 3: Inheritance

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: David Liu, Sophia Huynh

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 David Liu, Sophia Huynh

=== Module description ===
This module contains sample tests for Prep 3.
Complete the TODO in this file.

When writing a test case, make sure you create a new function, with its
name starting with "test_". For example:

def test_my_test_case():
    # Your test here
"""
from datetime import date
from hypothesis import given
from hypothesis.strategies import integers, floats
from prep3 import SalariedEmployee, HourlyEmployee, Company

# === Sample test cases below ===
# Use the below test cases as an example for writing your own test cases,
# and as a start to testing your prep3.py code.

# WARNING: THIS IS CURRENTLY AN EXTREMELY INCOMPLETE SET OF TESTS!
# We will test your code on a much more thorough set of tests!
@given(salary=floats(min_value=1))
def test_random_total_pay_salary_employee(salary: float) -> None:
    e = SalariedEmployee(13, 'William the human', salary)
    e.pay(date(2018, 6, 28))
    e.pay(date(2018, 7, 28))
    e.pay(date(2018, 8, 28))
    assert e.total_pay() == round(salary / 12, 2) * 3


@given(hourly_wage=floats(min_value=1), hours_per_month=integers(min_value=1))
def test_random_total_pay_hourly_employee(
        hourly_wage: float,
        hours_per_month: int) -> None:
    e = HourlyEmployee(15, 'Kexin the dog', hourly_wage, hours_per_month)
    e.pay(date(2018, 6, 28))
    e.pay(date(2018, 7, 28))
    e.pay(date(2018, 8, 28))
    assert e.total_pay() == round(hours_per_month * hourly_wage, 2) * 3


def test_total_pay_basic() -> None:
    e = SalariedEmployee(14, 'Gilbert the cat', 1200.0)
    e.pay(date(2018, 6, 28))
    e.pay(date(2018, 7, 28))
    e.pay(date(2018, 8, 28))
    assert e.total_pay() == 300.0


def test_total_payroll_mixed() -> None:
    my_corp = Company([SalariedEmployee(24, 'Gilbert the cat', 1200.0),
                       HourlyEmployee(25, 'Chairman Meow', 500.25, 1.0)])
    my_corp.pay_all(date(2018, 6, 28))
    assert my_corp.total_payroll() == 600.25


if __name__ == '__main__':
    import pytest

    pytest.main(['prep3_starter_tests.py'])
