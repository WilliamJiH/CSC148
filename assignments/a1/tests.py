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
def valid_answers_2() -> List[List[survey.Answer]]:
    return [[survey.Answer('a'), survey.Answer('a'),
             survey.Answer('a'), survey.Answer('a')],
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


@pytest.fixture
def group(students) -> grouper.Group:
    return grouper.Group(students)


@pytest.fixture
def duplicate_group(duplicate_students) -> grouper.Group:
    return grouper.Group(duplicate_students)


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


def test_slice_list():
    lst = []
    new = grouper.slice_list(lst, 1)
    assert new == []


def test_slice_list_2():
    lst = [1, 8, 0, 4, 2]
    assert grouper.slice_list(lst, 2) == [[1, 8], [0, 4], [2]]


def test_windows():
    lst = []
    new = grouper.windows(lst, 1)
    assert new == []


def test_windows_2():
    lst = [1, 0, 4, 9, 2]
    assert grouper.windows(lst, 3) == [[1, 0, 4], [0, 4, 9], [4, 9, 2]]


def test_windows_3():
    lst = [1, 0, True, 'f', 2]
    assert grouper.windows(lst, 3) == [[1, 0, True], [0, True, 'f'], [True, 'f', 2]]


class TestGroup:
    def test__len__(self, group):
        assert len(group) == 4

    def test__len__2(self, duplicate_group):
        assert len(duplicate_group) == 4

    def test__contains__(self, group, students):
        for student in students:
            assert student in group

    def test__contains__2(self, duplicate_group, duplicate_students):
        for student in duplicate_students:
            assert student in duplicate_group

    def test__str__(self, group, students):
        for student in students:
            assert student.name in str(group)

    def test__str__2(self, duplicate_group, duplicate_students):
        for student in duplicate_students:
            assert student.name in str(duplicate_group)

    def test_get_members(self, group, students):
        copy = group._members
        for student in students:
            assert student in grouper.Group.get_members(group)
        assert copy == group._members


class TestAnswer:
    def test_is_valid(self, valid_answers, questions):
        for i, question in enumerate(questions):
            assert valid_answers[i][0].is_valid(question)

    def test_is_valid_2(self, invalid_answers, questions):
        assert not invalid_answers[0][0].is_valid(questions[0])


class TestMultipleChoiceQuestion:
    def test__str__(self, questions):
        assert "Which one" in str(questions[0])

    def test_validate_answer(self, questions, valid_answers):
        qs = questions[0]
        assert qs.validate_answer(valid_answers[0][0])

    def test_validate_answer_not(self, questions, invalid_answers):
        qs = questions[0]
        assert not qs.validate_answer(invalid_answers[0][0])

    def test_get_similarity(self, questions, valid_answers):
        qs = questions[0]
        assert qs.get_similarity(*valid_answers[0][:2]) == 0.0

    def test_get_similarity_2(self, questions, valid_answers_2):
        qs = questions[0]
        assert qs.get_similarity(*valid_answers_2[0][:2]) == 1.0




if __name__ == '__main__':
    pytest.main(['tests.py'])
