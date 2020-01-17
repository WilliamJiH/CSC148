"""CSC148 Assignment 0: Sample tests

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Assignment 0.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests and to be confident your code is correct.

Note: this file is to only help you; you will not submit it when you hand in
the assignment.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Mario Badr, Christine Murad, Diane Horton, Misha Schwartz, Sophia Huynh
and Jaisie Sin

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Christine Murad, Diane Horton, Misha Schwartz,
Sophia Huynh and Jaisie Sin
"""
from datetime import datetime
from gym import WorkoutClass, Instructor, Gym


def test_instructor_attributes() -> None:
    """Test the public attributes of a new instructor."""
    instructor = Instructor(5, 'Matthew')
    assert instructor.get_id() == 5
    assert instructor.name == 'Matthew'


def test_instructor_one_certificate_get_certificates() -> None:
    """Test Instructor.get_num_certificates with a single certificate."""
    instructor = Instructor(5, 'Matthew')
    assert instructor.add_certificate('Kickboxing')
    assert instructor.get_num_certificates() == 1


def test_instructor_one_certificate_can_teach() -> None:
    """Test Instructor.can_teach with a single satisfying certificate."""
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    assert instructor.add_certificate('Lifeguard')
    assert instructor.can_teach(swimming)


def test_gym_register_one_class() -> None:
    """Test Gym.register with a single user and class."""
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert instructor.add_certificate('Lifeguard')
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.register(jan_28_2020_11_00, 'Benjamin', 'Swimming')


def test_gym_offerings_at_one_class() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', ['Lifeguard'])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert instructor.add_certificate('Lifeguard')
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    assert ac.offerings_at(jan_28_2020_11_00) == \
        [('Matthew', 'Swimming', '25-yard Pool')]


def test_gym_one_instructor_one_hour_pay_no_certificates() -> None:
    ac = Gym('Athletic Centre')
    instructor = Instructor(5, 'Matthew')
    swimming = WorkoutClass('Swimming', [])
    jan_28_2020_11_00 = datetime(2020, 1, 29, 11, 0)
    assert ac.add_workout_class(swimming)
    assert ac.add_instructor(instructor)
    assert ac.add_room('25-yard Pool', 100)
    assert ac.schedule_workout_class(jan_28_2020_11_00, '25-yard Pool',
                                     swimming.get_name(), instructor.get_id())
    t1 = datetime(2020, 1, 17, 11, 0)
    t2 = datetime(2020, 1, 29, 13, 0)
    assert ac.payroll(t1, t2, 22.0) == [(5, 'Matthew', 1, 22)]


if __name__ == '__main__':
    import pytest
    pytest.main(['a0_sample_test.py'])
