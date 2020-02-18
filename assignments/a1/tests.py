# TODO: put all your tests in this file (you can delete this line)
import pytest
import course
import criterion
import grouper
import survey
from typing import List, Set, FrozenSet


def get_member_ids(grouping: grouper.Grouping) -> Set[FrozenSet[int]]:
    member_ids = set()
    for group in grouping.get_groups():
        ids = []
        for member in group.get_members():
            ids.append(member.id)
        member_ids.add(frozenset(ids))
    return member_ids


def compare_groupings(grouping1: grouper.Grouping,
                      grouping2: grouper.Grouping) -> None:
    assert get_member_ids(grouping1) == get_member_ids(grouping2)


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
def greedy_grouping(students_with_valid_answers) -> grouper.Grouping:
    grouping = grouper.Grouping()
    grouping.add_group(grouper.Group([students_with_valid_answers[0],
                                      students_with_valid_answers[1]]))
    grouping.add_group(grouper.Group([students_with_valid_answers[2],
                                      students_with_valid_answers[3]]))
    return grouping


@pytest.fixture
def greedy_grouping_2(students_with_valid_answers) -> grouper.Grouping:
    grouping = grouper.Grouping()
    grouping.add_group(grouper.Group([students_with_valid_answers[0],
                                      students_with_valid_answers[1],
                                      students_with_valid_answers[3]]))
    grouping.add_group(grouper.Group([students_with_valid_answers[2]]))
    return grouping


@pytest.fixture
def window_grouping(students_with_valid_answers) -> grouper.Grouping:
    grouping = grouper.Grouping()
    grouping.add_group(grouper.Group([students_with_valid_answers[0],
                                      students_with_valid_answers[1]]))
    grouping.add_group(grouper.Group([students_with_valid_answers[2],
                                      students_with_valid_answers[3]]))
    return grouping


@pytest.fixture
def window_grouping_2(students_with_valid_answers) -> grouper.Grouping:
    grouping = grouper.Grouping()
    grouping.add_group(grouper.Group([students_with_valid_answers[1],
                                      students_with_valid_answers[2],
                                      students_with_valid_answers[3]]))
    grouping.add_group(grouper.Group([students_with_valid_answers[0]]))
    return grouping


@pytest.fixture
def alpha_grouping(students_with_valid_answers) -> grouper.Grouping:
    grouping = grouper.Grouping()
    grouping.add_group(grouper.Group([students_with_valid_answers[0],
                                      students_with_valid_answers[2]]))
    grouping.add_group(grouper.Group([students_with_valid_answers[1],
                                      students_with_valid_answers[3]]))
    return grouping


@pytest.fixture
def alpha_grouping_2(students_with_valid_answers) -> grouper.Grouping:
    grouping = grouper.Grouping()
    grouping.add_group(grouper.Group([students_with_valid_answers[0],
                                      students_with_valid_answers[2],
                                      students_with_valid_answers[3]]))
    grouping.add_group(grouper.Group([students_with_valid_answers[1]]))
    return grouping


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
             survey.Answer(['c', 'd']), survey.Answer(['c', 'd'])]]


@pytest.fixture
def valid_answers_2() -> List[List[survey.Answer]]:
    return [[survey.Answer('a'), survey.Answer('a'),
             survey.Answer('a'), survey.Answer('a')],
            [survey.Answer(1), survey.Answer(1),
             survey.Answer(1), survey.Answer(5)],
            [survey.Answer(True), survey.Answer(True),
             survey.Answer(True), survey.Answer(True)],
            [survey.Answer(['a', 'b']), survey.Answer(['a', 'b', 'c']),
             survey.Answer(['c', 'd']), survey.Answer(['a', 'b'])]]


@pytest.fixture
def single_answer() -> List[List[survey.Answer]]:
    return [[survey.Answer('a')], [survey.Answer(1)],
            [survey.Answer(True)], [survey.Answer(['a', 'b'])]]


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


@pytest.fixture
def criteria(valid_answers) -> List[criterion.Criterion]:
    return [criterion.HomogeneousCriterion(),
            criterion.HeterogeneousCriterion(),
            criterion.LonelyMemberCriterion()]


@pytest.fixture
def weights() -> List[int]:
    return [2, 3, 4]


@pytest.fixture
def survey_(questions, criteria, weights) -> survey.Survey:
    s = survey.Survey(questions)
    for i, question in enumerate(questions):
        if i:
            s.set_weight(weights[i - 1], question)
        if len(questions) - 1 != i:
            s.set_criterion(criteria[i], question)
    return s


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

    def test_all_answered(self, course_with_students_with_valid_answers,
                          survey_):
        assert course_with_students_with_valid_answers.all_answered(survey_)

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
    assert grouper.windows(lst, 3) == [[1, 0, True], [0, True, 'f'],
                                       [True, 'f', 2]]


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


class TestNumericQuestion:
    def test__str__(self, questions):
        assert 'How many digit' in str(questions[1])

    def test_validate_answer(self, questions, valid_answers):
        qs = questions[1]
        assert qs.validate_answer(valid_answers[1][0])

    def test_validate_answer_not(self, questions, invalid_answers):
        qs = questions[1]
        assert not qs.validate_answer(invalid_answers[1][0])

    def test_get_similarity(self, questions, valid_answers):
        qs = questions[1]
        similarity = qs.get_similarity(*valid_answers[1][:2])
        assert round(similarity, 2) == 0.75

    def test_get_similarity_2(self, questions, valid_answers_2):
        qs = questions[1]
        similarity = qs.get_similarity(*valid_answers_2[1][:2])
        assert round(similarity, 2) == 1.0

    def test_get_similarity_3(self, questions, valid_answers_2):
        qs = questions[1]
        similarity = qs.get_similarity(*valid_answers_2[1][2:])
        assert round(similarity, 2) == 0.0


class TestYesNoQuestion:
    def test__str__(self, questions):
        assert 'Yes or No' in str(questions[2])

    def test_validate_answer(self, questions, valid_answers):
        assert questions[2].validate_answer(valid_answers[2][0])

    def test_validate_answer_not(self, questions, invalid_answers):
        qs = questions[2]
        assert not qs.validate_answer(invalid_answers[2][0])

    def test_get_similarity(self, questions, valid_answers):
        qs = questions[2]
        similarity = qs.get_similarity(*valid_answers[2][:2])
        assert round(similarity, 2) == 0.0

    def test_get_similarity_2(self, questions, valid_answers_2):
        qs = questions[2]
        similarity = qs.get_similarity(*valid_answers_2[2][:2])
        assert round(similarity, 2) == 1.0


class TestCheckboxQuestion:
    def test__str__(self, questions):
        assert 'Choose more' in str(questions[3])

    def test_validate_answer(self, questions, valid_answers):
        assert questions[3].validate_answer(valid_answers[3][0])

    def test_validate_answer_not(self, questions, invalid_answers):
        assert not questions[3].validate_answer(invalid_answers[3][0])

    def test_get_similarity(self, questions, valid_answers):
        qs = questions[3]
        similarity = qs.get_similarity(*valid_answers[3][:2])
        assert similarity == 2 / 3

    def test_get_similarity_2(self, questions, valid_answers):
        qs = questions[3]
        similarity = qs.get_similarity(*valid_answers[3][2:])
        assert similarity == 1

    def test_get_similarity_3(self, questions, valid_answers_2):
        qs = questions[3]
        similarity = qs.get_similarity(*valid_answers_2[3][2:])
        assert similarity == 0


class TestHomogeneousCriterion:
    def test_score_answers(self, criteria, valid_answers, questions):
        cri = criteria[0]
        score = cri.score_answers(questions[0], valid_answers[0])
        assert round(score, 2) == 0.17

    def test_score_answers_2(self, criteria, valid_answers_2, questions):
        cri = criteria[0]
        score = cri.score_answers(questions[1], valid_answers_2[1])
        assert round(score, 2) == 0.5

    def test_score_answers_single(self, criteria, single_answer, questions):
        cri = criteria[0]
        score = cri.score_answers(questions[1], single_answer[1])
        assert score == 1.0

    def test_score_answers_invalid(self, criteria, invalid_answers, questions):
        cri = criteria[0]
        try:
            cri.score_answers(questions[0], invalid_answers[0])
            assert False
        except criterion.InvalidAnswerError:
            assert True


class TestHeterogeneousCriterion:
    def test_score_answers(self, criteria, valid_answers, questions):
        cri = criteria[1]
        score = cri.score_answers(questions[0], valid_answers[0])
        assert round(score, 2) == 0.83

    def test_score_answers_2(self, criteria, valid_answers_2, questions):
        cri = criteria[1]
        score = cri.score_answers(questions[1], valid_answers_2[1])
        assert round(score, 2) == 0.5

    def test_score_answers_single(self, criteria, single_answer, questions):
        cri = criteria[1]
        score = cri.score_answers(questions[1], single_answer[1])
        assert score == 0.0

    def test_score_answers_invalid(self, criteria, invalid_answers, questions):
        cri = criteria[1]
        try:
            cri.score_answers(questions[0], invalid_answers[0])
            assert False
        except criterion.InvalidAnswerError:
            assert True


class TestLonelyMemberCriterion:
    def test_score_answers(self, criteria, valid_answers, questions):
        cri = criteria[2]
        score = cri.score_answers(questions[0], valid_answers[0])
        assert round(score, 2) == 0.0

    def test_score_answers_2(self, criteria, valid_answers_2, questions):
        cri = criteria[2]
        score = cri.score_answers(questions[1], valid_answers_2[1])
        assert round(score, 2) == 0.0

    def test_score_answers_single(self, criteria, single_answer, questions):
        cri = criteria[2]
        score = cri.score_answers(questions[1], single_answer[1])
        assert score == 0.0

    def test_score_answers_single_same(self, criteria, valid_answers_2,
                                       questions):
        cri = criteria[2]
        score = cri.score_answers(questions[2], valid_answers_2[2])
        assert score == 1.0

    def test_score_answers_invalid(self, criteria, invalid_answers, questions):
        cri = criteria[2]
        try:
            cri.score_answers(questions[0], invalid_answers[0])
            assert False
        except criterion.InvalidAnswerError:
            assert True


class TestSurvey:
    def test___len__(self, survey_):
        assert len(survey_) == 4

    def test___contains__(self, survey_, questions):
        for question in questions:
            assert question in survey_

    def test__str__(self, survey_, questions):
        for question in questions:
            assert str(question) in str(survey_)

    def test_get_questions(self, survey_, questions):
        q_ = []
        for question in questions:
            q_.append(question)
        for question in survey_.get_questions():
            assert question in q_

    def test__get_criterion(self, survey_, questions, criteria):
        criteria.append(criterion.HomogeneousCriterion())
        for i, question in enumerate(questions):
            assert isinstance(survey_._get_criterion(question),
                              type(criteria[i]))

    def test__get_criterion_default(self, survey_, questions, criteria):
        assert isinstance(survey_._get_criterion(questions[-1]),
                          type(criteria[0]))

    def test__get_weight(self, survey_, questions, weights):
        weights.insert(0, 1)
        for i, question in enumerate(questions):
            assert isinstance(survey_._get_weight(question), type(weights[i]))

    def test__get_weight_default(self, survey_, questions):
        assert survey_._get_weight(questions[0]) == 1

    def test__get_weight_2(self, survey_, questions, weights):
        for i, question in enumerate(questions):
            try:
                isinstance(survey_._get_weight(question), type(weights[i]))
                assert True
            except IndexError:
                assert True

    def test_set_weight(self, survey_, questions):
        survey_.set_weight(9, questions[0])
        assert survey_._get_weight(questions[0]) == 9

    def test_set_weight_2(self, survey_):
        question1 = survey.YesNoQuestion(100, 'Y or N')
        assert not survey_.set_weight(2, question1)

    def test_set_criterion(self, survey_, questions):
        cri = criterion.HeterogeneousCriterion()
        survey_.set_criterion(cri, questions[0])
        assert survey_._get_criterion(questions[0]) == cri

    def test_set_criterion_2(self, survey_):
        question1 = survey.YesNoQuestion(19, 'YYY')
        assert not survey_.set_criterion(criterion.HomogeneousCriterion,
                                         question1)

    def test_score_students(self, survey_, students_with_valid_answers):
        score = survey_.score_students(students_with_valid_answers)
        assert round(score, 2) == 1.42

    def test_score_students_2(self, survey_, students_with_invalid_answers):
        score = survey_.score_students(students_with_invalid_answers)
        assert score == 0

    def test_score_grouping(self, survey_, alpha_grouping):
        score = survey_.score_grouping(alpha_grouping)
        assert round(score, 2) == 1.06


class TestAlphaGrouper:
    def test_make_grouping(self, course_with_students_with_valid_answers,
                           alpha_grouping, survey_):
        grouper_ = grouper.AlphaGrouper(2)
        grouping = grouper_.make_grouping(
            course_with_students_with_valid_answers,
            survey_)
        compare_groupings(grouping, alpha_grouping)

    def test_make_grouping_2(self, course_with_students_with_valid_answers,
                             alpha_grouping_2, survey_):
        grouper_ = grouper.AlphaGrouper(3)
        grouping = grouper_.make_grouping(
            course_with_students_with_valid_answers,
            survey_)
        compare_groupings(alpha_grouping_2, grouping)


class TestRandomGrouper:
    def test_make_grouping(self, course_with_students_with_valid_answers,
                           survey_) -> None:
        grouper_ = grouper.RandomGrouper(2)
        grouping = grouper_.make_grouping(
            course_with_students_with_valid_answers,
            survey_)
        member_ids = get_member_ids(grouping)
        assert len(member_ids) == 2
        for ids in member_ids:
            assert len(ids) == 2
        assert len(frozenset.intersection(*member_ids)) == 0


class TestGreedyGrouper:
    def test__get_pos(self):
        s = grouper.GreedyGrouper(2)
        lst = [(1, 1.0), (2, 3.5), (3, 0.9)]
        assert s._get_pos(lst) == 2

    def test__get_pos_2(self):
        s = grouper.GreedyGrouper(2)
        lst = [(1, 1.0), (2, 0.5), (3, 10)]
        assert s._get_pos(lst) == 3

    def test__get_pos_3(self):
        s = grouper.GreedyGrouper(2)
        lst = [(1, 0.1)]
        assert s._get_pos(lst) == 1

    def test_make_grouping(self, course_with_students_with_valid_answers,
                           greedy_grouping, survey_):
        grouper_ = grouper.GreedyGrouper(2)
        grouping1 = grouper_.make_grouping(
            course_with_students_with_valid_answers,
            survey_)
        compare_groupings(grouping1, greedy_grouping)

    def test_make_grouping_2(self, course_with_students_with_valid_answers,
                             greedy_grouping_2, survey_):
        grouper_ = grouper.GreedyGrouper(3)
        grouping1 = grouper_.make_grouping(
            course_with_students_with_valid_answers,
            survey_)
        compare_groupings(grouping1, greedy_grouping_2)


class TestWindowGrouper:
    def test_make_grouping(self, course_with_students_with_valid_answers,
                           window_grouping, survey_):
        grouper_ = grouper.WindowGrouper(2)
        grouping = grouper_.make_grouping(
            course_with_students_with_valid_answers,
            survey_)
        compare_groupings(grouping, window_grouping)

    def test_make_grouping_2(self, course_with_students_with_valid_answers,
                             window_grouping_2, survey_):
        grouper_ = grouper.WindowGrouper(3)
        grouping = grouper_.make_grouping(
            course_with_students_with_valid_answers,
            survey_)
        compare_groupings(window_grouping_2, grouping)


class TestGrouping:
    def test__len__(self, alpha_grouping):
        assert len(alpha_grouping) == 2

    def test__len__2(self, alpha_grouping_2):
        assert len(alpha_grouping_2) == 2

    def test__str__(self, alpha_grouping):
        lines = str(alpha_grouping).splitlines()
        assert len(lines) == 2

        in_lines = []
        for group in alpha_grouping.get_groups():
            in_line = []
            for members in group.get_members():
                name = members.name
                assert name in str(alpha_grouping)
                if name in lines[0]:
                    in_line.append(0)
                    assert name not in lines[1]
                if name in lines[1]:
                    in_line.append(1)
                    assert name not in lines[0]
            assert len(set(in_line)) == 1
            assert in_line[0] not in in_lines
            in_lines.append(in_line[0])

    def test_add_group(self, group):
        grouping = grouper.Grouping()
        grouping.add_group(group)
        assert group in grouping._groups

    def test_add_group_empty(self):
        grouping = grouper.Grouping()
        assert not grouping.add_group(grouper.Group([]))

    def test_add_group_duplicate(self, group):
        grouping = grouper.Grouping()
        group1 = group
        grouping.add_group(group)
        assert not grouping.add_group(group1)

    def test_get_groups(self, students):
        group = grouper.Group(students[:2])
        grouping = grouper.Grouping()
        grouping.add_group(group)
        assert get_member_ids(grouping) == {frozenset([1, 2])}

    def test_get_groups_all(self, students):
        group = grouper.Group(students)
        grouping = grouper.Grouping()
        grouping.add_group(group)
        assert get_member_ids(grouping) == {frozenset([1, 2, 3, 4])}


if __name__ == '__main__':
    pytest.main(['tests.py'])
