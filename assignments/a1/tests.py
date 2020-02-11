import course
import survey
import criterion
import grouper
import pytest
from typing import List


@pytest.fixture
def course148() -> course.Course:
    return course.Course('CSC148')


@pytest.fixture
def new_students() -> List[course.Student]:
    return [course.Student(1, 'Gary'), course.Student(2, 'Dino'),
            course.Student(3, 'William'), course.Student(4, 'Ziyue')]


@pytest.fixture
def course_with_students(course148, new_students) -> course.Course:
    course148.enroll_students(new_students)
    return course148


class TestCourse:
    def test_enroll_students(self, course148, new_students) -> None:
        course148.enroll_students(new_students)
        for student in new_students:
            assert student in course148.students

    def test_all_answered(self) -> None:
        pass

    def test_get_students(self, course_with_students) -> None:
        students = course_with_students.get_students()
        for student in students:
            assert student in course_with_students.students


class TestStudent:
    def test___str__(self, new_students) -> None:
        student = new_students[0]
        assert student.name == str(student)

    def test_has_answer(self) -> None:
        pass

    def test_set_answer(self) -> None:
        pass

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
