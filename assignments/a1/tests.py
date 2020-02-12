import course
import survey
import criterion
import grouper
import pytest
from typing import List


@pytest.fixture
def empty_course() -> course.Course:
    return course.Course("CSC148")


@pytest.fixture
def students() -> List[course.Student]:
    return [course.Student(1, 'Gary'), course.Student(2, 'Dino'),
            course.Student(3, 'William'), course.Student(4, 'Ziyue')]


@pytest.fixture
def duplicate_students() -> List[course.Student]:
    return [course.Student(5, 'Anny'), course.Student(5, 'Anny'),
            course.Student(6, 'Nick'), course.Student(7, 'Diane')]


@pytest.fixture
def questions() -> List[survey.Question]:
    return [
        survey.MultipleChoiceQuestion(
            1, 'MultipleChoiceQuestion', [
                'A', 'B']), survey.NumericQuestion(
            2, 'NumericQuestion?', -1, 2), survey.YesNoQuestion(
            3, 'YesNoQuestion'), survey.CheckboxQuestion(
            4, 'CheckboxQuestion', [
                'B', 'C'])]


@pytest.fixture
def answers() -> List[List[survey.Answer]]:
    return [[survey.Answer('A'), survey.Answer('B'),
             survey.Answer('A'), survey.Answer('B')],
            [survey.Answer(-1), survey.Answer(0),
             survey.Answer(1), survey.Answer(2)],
            [survey.Answer(True), survey.Answer(False),
             survey.Answer(True), survey.Answer(False)],
            [survey.Answer(['B', 'C']), survey.Answer(['B', 'C']),
             survey.Answer(['B']), survey.Answer(['C'])]]


# @pytest.fixture
# def students_with_answers(students, questions, answers) -> List[course.Student]:
#     for i, student in enumerate(students):
#         for j, question in enumerate(questions):
#             student.set_answer(question, answers[j][i])
#     return students


# @pytest.fixture
# def course_with_students_with_answers(empty_course,
#                                       students_with_answers) -> course.Course:
#     empty_course.enroll_students(students_with_answers)
#     return empty_course


class TestCourse:
    def test_enroll_students(self, empty_course, students) -> None:
        empty_course.enroll_students(students)
        for student in students:
            assert student in empty_course.students

    def test_enroll_duplicate_students(
            self, empty_course, duplicate_students) -> None:
        empty_course.enroll_students(duplicate_students)
        assert len(empty_course.students) == 0

    def test_enroll_students_after_student_not_empty(
            self, empty_course, students):
        empty_course.enroll_students(students)
        assert len(empty_course.students) == 4
        empty_course.enroll_students([course.Student(8, 'Max'), course.Student(
            9, 'Andrew'), course.Student(10, 'Ray'),
                                      course.Student(11, 'Charles')])
        assert len(empty_course.students) == 8

    def test_enroll_empty_students_after_student_not_empty(
            self, empty_course, students):
        empty_course.enroll_students(students)
        assert len(empty_course.students) == 4
        empty_course.enroll_students([])
        assert len(empty_course.students) == 4

    def test_all_answered(self) -> None:
        pass

    def test_get_students(self, empty_course, students) -> None:
        empty_course.enroll_students(students)
        for student in students:
            assert student in empty_course.students

    def test_get_empty_students(self, empty_course) -> None:
        empty_course.enroll_students([])
        assert len(empty_course.get_students()) == 0


class TestStudent:
    def test___str__(self, students) -> None:
        assert students[0].name == str(students[0])
        assert students[1].name == str(students[1])
        assert students[2].name == str(students[2])
        assert students[3].name == str(students[3])

    def test_has_answer(self, students, questions, answers) -> None:
        students[0].set_answer(questions[0], answers[0][0])
        assert students[0].has_answer(questions[0]) is True

    def test_set_single_answer(self, students, questions, answers) -> None:
        students[0].set_answer(questions[0], answers[0][0])
        assert students[0]._answers[questions[0].id] == answers[0][0]
        assert len(students[0]._answers) == 1

    # get_answer/ has_answer 有问题
    def test_set_multiple_answers(self, students, questions, answers) -> None:
        for i, student in enumerate(students):
            for j, question in enumerate(questions):
                answer = answers[j][i]
                student.set_answer(question, answer)
                assert student.get_answer(question) == answer

    def test_get_answer(self) -> None:
        pass


class TestHomogeneousCriterion:
    def test_score_answers(self) -> None:
        pass


class TestHeterogeneousCriterion:
    def test_score_answers(self) -> None:
        pass


class TestLonelyMemberCriterion:
    def test_score_answers(self) -> None:
        pass


def test_slice_list() -> None:
    lst = list(range(7))
    assert grouper.slice_list(lst, 3) == [[0, 1, 2], [3, 4, 5], [6]]


def test_windows() -> None:
    lst = list(range(5))
    assert grouper.windows(lst, 3) == [[0, 1, 2], [1, 2, 3], [2, 3, 4]]


class TestAlphaGrouper:
    def test_make_grouping(self) -> None:
        pass


class TestRandomGrouper:
    def test_make_grouping(self) -> None:
        pass


class TestGreedyGrouper:
    def test_make_grouping(self) -> None:
        pass


class TestWindowGrouper:
    def test_make_grouping(self) -> None:
        pass


class TestGroup:
    def test___len__(self) -> None:
        pass

    def test___contains__(self) -> None:
        pass

    def test___str__(self) -> None:
        pass

    def test_get_members(self) -> None:
        pass


class TestGrouping:
    def test___len__(self) -> None:
        pass

    def test___str__(self) -> None:
        pass

    def test_add_group(self) -> None:
        pass

    def test_get_groups(self) -> None:
        pass


class TestSurvey:
    def test___len__(self) -> None:
        pass

    def test___contains__(self) -> None:
        pass

    def test___str__(self) -> None:
        pass

    def test_get_questions(self) -> None:
        pass

    def test__get_criterion(self) -> None:
        pass

    def test__get_weight(self) -> None:
        pass

    def test_set_weight(self) -> None:
        pass

    def test_set_criterion(self) -> None:
        pass

    def test_score_students(self) -> None:
        pass

    def test_score_grouping(self) -> None:
        pass


class TestAnswer:
    def test_is_valid(self) -> None:
        pass


class TestMultipleChoiceQuestion:
    def test___str__(self) -> None:
        pass

    def test_validate_answer(self) -> None:
        pass

    def test_get_similarity(self) -> None:
        pass


class TestNumericQuestion:
    def test___str__(self) -> None:
        pass

    def test_validate_answer(self) -> None:
        pass

    def test_get_similarity(self) -> None:
        pass


class TestYesNoQuestion:
    def test___str__(self) -> None:
        pass

    def test_validate_answer(self) -> None:
        pass

    def test_get_similarity(self) -> None:
        pass


class TestCheckboxQuestion:
    def test___str__(self) -> None:
        pass

    def test_validate_answer(self) -> None:
        pass

    def test_get_similarity(self) -> None:
        pass


if __name__ == '__main__':
    pytest.main(['tests.py'])
