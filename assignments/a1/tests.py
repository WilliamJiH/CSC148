# TODO: put all your tests in this file (you can delete this line)
import pytest
import course
import criterion
import grouper
import survey
from typing import List, Set, FrozenSet


@pytest.fixture
def empty_course() -> course.Course:
    return course.Course('CSC165')


@pytest.fixture
def students() -> List[course.Student]:
    return [course.Student(1, 'Gary'), course.Student(2, 'William'),
            course.Student(3, 'Charles'), course.Student(4, 'Ted')]


@pytest.fixture
def duplicate_students() -> List[course.Student]:
    return [course.Student(1, 'Ann'), course.Student(1, 'Ann'),
            course.Student(2, 'Frank'), course.Student(3, 'Diane')]


@pytest.fixture
def course_with_students(empty_course, students) -> course.Course:
    empty_course.enroll_students(students)
    return empty_course


@pytest.fixture
def course_with_duplicate_students(empty_course,
                                   duplicate_students) -> course.Course:
    empty_course.enroll_students(duplicate_students)
    return empty_course


@pytest.fixture
def questions() -> List[survey.Question]:
    return [survey.MultipleChoiceQuestion(1, 'Which one?', ['a', 'b', 'c']),
            survey.NumericQuestion(2, 'How many digits?', 1, 5),
            survey.YesNoQuestion(3, 'Yes or No?'),
            survey.CheckboxQuestion(4, 'Choose more than one!',
                                    ['a', 'b', 'c', 'd'])]


@pytest.fixture
def valid_answers() -> List[List[survey.Answer]]:
    return [[survey.Answer('a'), survey.Answer('c'),
             survey.Answer('b'), survey.Answer('a')],
            [survey.Answer(1), survey.Answer(2),
             survey.Answer(1), survey.Answer(5)],
            [survey.Answer(True), survey.Answer(False),
             survey.Answer(True), survey.Answer(False)],
            [survey.Answer(['a', 'b']), survey.Answer(['a', 'b', 'c']),
             survey.Answer(['c', 'd']), survey.Answer(['a', 'd'])]]


@pytest.fixture
def invalid_answers() -> List[List[survey.Answer]]:
    return [[survey.Answer('d'), survey.Answer('c'),
             survey.Answer('a'), survey.Answer('a')],
            [survey.Answer(7), survey.Answer(2),
             survey.Answer(1), survey.Answer(1)],
            [survey.Answer('f'), survey.Answer(True),
             survey.Answer(True), survey.Answer(False)],
            [survey.Answer(['a', 'b', 'e']), survey.Answer(['a', 'b', 'c']),
             survey.Answer(['c', 'd']), survey.Answer(['a', 'd'])]]


@pytest.fixture
def students_with_valid_answers(students, questions, valid_answers) -> List[
    course.Student]:
    for i, student in enumerate(students):
        for j, question in enumerate(questions):
            student.set_answer(question, valid_answers[j][i])
    return students


@pytest.fixture
def students_with_invalid_answers(students, questions, invalid_answers) -> List[
    course.Student]:
    for i, student in enumerate(students):
        for j, question in enumerate(questions):
            student.set_answer(question, invalid_answers[j][i])
    return students


@pytest.fixture
def course_with_students_with_valid_answers(empty_course,
                                            students_with_valid_answers):
    empty_course.enroll_students(students_with_valid_answers)
    return empty_course


@pytest.fixture
def course_with_students_with_invalid_answers(empty_course,
                                              students_with_invalid_answers):
    empty_course.enroll_students(students_with_invalid_answers)
    return empty_course


class TestStudent:
    def test__str__(self, students):
        a = students[0]
        assert a.name == str(a)

    def test__str__2(self, duplicate_students):
        a = duplicate_students[1]
        assert a.name == str(a)

    def test_has_answer(self, students_with_valid_answers, questions):
        for student in students_with_valid_answers:
            for question in questions:
                assert student.has_answer(question)

    def test_has_answer_invalid(self, students_with_invalid_answers, questions):
        for question in questions:
            assert not students_with_invalid_answers[0].has_answer(question)

    def test_set_answer(self, students, questions, valid_answers):
        for i, student in enumerate(students):
            for j, question in enumerate(questions):
                answer = valid_answers[j][i]
                student.set_answer(question, answer)
                assert student.get_answer(question) == answer

    def test_get_answer(self, students_with_valid_answers, questions,
                        valid_answers):
        for i, student in enumerate(students_with_valid_answers):
            for j, question in enumerate(questions):
                assert student.get_answer(question) == valid_answers[j][i]

    def test_get_answer_no(self, students, questions):
        for i, student in enumerate(students):
            for j, question in enumerate(questions):
                assert student.get_answer(question) is None


class TestCourse:
    def test_enroll_students(self, empty_course, students):
        empty_course.enroll_students(students)
        for student in students:
            assert student in empty_course.students

    def test_enroll_students_2(self, empty_course, duplicate_students):
        empty_course.enroll_students(duplicate_students)
        for student in duplicate_students:
            assert student not in empty_course.students

    def test_all_answered(self, course_with_students_with_valid_answers):
        # assert course_with_students_with_valid_answers.all_answered()
        pass

    def test_get_students(self, course_with_students):
        students = course_with_students.get_students()
        assert len(students) == 4

    def test_get_students_dup(self, course_with_duplicate_students):
        dup_students = course_with_duplicate_students.get_students()
        assert len(dup_students) == 0


if __name__ == '__main__':
    pytest.main(['tests.py'])
