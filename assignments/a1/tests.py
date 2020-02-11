import unittest
from course import *
from survey import *
from criterion import *
from grouper import *


class Test_Student(unittest.TestCase):

    def test_student_has_answer(self):
        pass

    def test_student_set_answer(self):
        pass

    def test_student_get_answer(self):
        pass


class Test_Course(unittest.TestCase):

    def test_course_enroll_students(self):
        pass

    def test_course_all_answered(self):
        pass

    def test_course_get_students(self):
        pass


class Test_Question(unittest.TestCase):

    def test_question_(self):
        pass


class Test_Survey(unittest.TestCase):

    def test_survey_set_default_criterion(self):
        pass

    def test_survey_set_default_weight(self):
        pass

    def test_survey_get_question(self):
        pass

    def test_survey__get_criterion(self):
        pass

    def test_survey__get_weight(self):
        pass

    def test_survey_set_weight(self):
        pass

    def test_survey_set_criterion(self):
        pass

    def test_survey_score_students(self):
        pass

    def test_survey_score_grouping(self):
        pass
