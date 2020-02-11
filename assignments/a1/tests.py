class Test_Student:

    def test_student_has_answer(self):
        pass

    def test_student_set_answer(self):
        pass

    def test_student_get_answer(self):
        pass


class Test_Course:

    def test_course_enroll_students(self):
        pass

    def test_course_all_answered(self):
        pass

    def test_course_get_students(self):
        pass


class Test_Question:

    def test_question_(self):
        pass


class Test_Survey:

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


if __name__ == '__main__':
    import pytest
    import course
    import survey
    import criterion
    import grouper

    pytest.main(['tests.py'])
