import unittest
import gym
from gym import *

gym.BONUS_RATE = 3


class TestInstructor(unittest.TestCase):
    def setUp(self) -> None:
        def assert_fun(instructor, val):
            self.assertEqual(instructor.name, val[0])
            self.assertEqual(instructor.get_id(), val[1])
            self.assertEqual(instructor.get_num_certificates(), val[2])

        self.instructor = Instructor(1, 'Diane')
        self.assert_fun = assert_fun

    def tearDown(self) -> None:
        self.instructor = Instructor(1, 'Diane')

    def test_no_public_method(self):
        temp = Instructor.__dict__
        attrs = list(temp.keys())
        public_attrs = sorted(list(filter(lambda x: "__" not in x, attrs)))
        self.assertListEqual(
            public_attrs, [
                "add_certificate", "can_teach", "get_id",
                "get_num_certificates"])

    def test_setup(self) -> None:
        self.assert_fun(self.instructor, ['Diane', 1, 0])

    def test_add_certificate(self):
        input_list = ["Computer Science"] * 3 + ["DataBase"] * 3 + ["PLT"] * 3
        for i in range(len(input_list)):
            assert_fun = self.assertTrue if i % 3 == 0 else self.assertFalse
            verify_list = ["Diane", 1, (i // 3) + 1]
            assert_fun(self.instructor.add_certificate(input_list[i]))
            self.assert_fun(self.instructor, verify_list)

    def test_can_teach_1(self):
        workout = WorkoutClass("Computer Science", [])
        self.assertTrue(self.instructor.can_teach(workout))
        workout2 = WorkoutClass("Computer Science", ["Intro to Com Science"])
        self.assertFalse(self.instructor.can_teach(workout2))

    def test_can_teach_2(self):
        workout = WorkoutClass(
            "Computer Science", [
                "Intro to Com Sci", "Intro to Soft Eng"])
        self.instructor.add_certificate("Intro to Com Sci")
        self.assertFalse(self.instructor.can_teach(workout))
        self.assert_fun(self.instructor, ["Diane", 1, 1])
        self.instructor.add_certificate("Intro to Soft Eng")
        self.assert_fun(self.instructor, ["Diane", 1, 2])
        self.assertTrue(self.instructor.can_teach(workout))
        self.instructor.add_certificate("Intro to DB")
        self.assert_fun(self.instructor, ["Diane", 1, 3])
        self.assertTrue(self.instructor.can_teach(workout))


class TestGym(unittest.TestCase):
    def setUp(self) -> None:
        self.gym = Gym("gym")
        self.instructor1 = Instructor(1, "Diane")
        self.instructor2 = Instructor(2, "David")
        self.workout1 = WorkoutClass("Intro to Com Sci", [])
        self.workout2 = WorkoutClass("Intro to SE", ["Intro to Com Sci"])
        self.msg = "Expected value is {} actual value is {}".format

    def tearDown(self) -> None:
        self.gym = Gym("gym")
        self.instructor1 = Instructor(1, "Diane")
        self.instructor2 = Instructor(2, "David")
        self.workout1 = WorkoutClass("Intro to Com Sci", [])
        self.workout2 = WorkoutClass("Intro to SE", ["Intro to Com Sci"])

    def test_setup(self):
        attrs = list(self.gym.__dict__)
        self.assertTrue(self.gym.name == "gym")
        self.assertTrue(len(list(filter(lambda x: x != "name", attrs))) >= 4)

    def test_no_public_method(self):
        temp = Gym.__dict__
        attrs = list(temp.keys())
        public_attrs = sorted(list(filter(lambda x: "__" not in x, attrs)))
        self.assertListEqual(public_attrs,
                             ["add_instructor",
                              "add_room",
                              "add_workout_class",
                              "instructor_hours",
                              "offerings_at",
                              "payroll",
                              "register",
                              "schedule_workout_class"])

    def test_add_instructor(self):
        instructor3 = self.instructor1
        self.assertTrue(self.gym.add_instructor(self.instructor1))
        self.assertFalse(self.gym.add_instructor(self.instructor1))
        self.assertTrue(self.gym.add_instructor(self.instructor2))
        self.assertFalse(self.gym.add_instructor(instructor3))

    def test_add_room(self):
        rooms = [("AC", 100), ("AC", 200), ("BA", 100),
                 ("BA", 200), ("UC", 100), ("UC", 200)]
        for i in range(len(rooms)):
            room = rooms[i]
            assert_fun = self.assertTrue if i % 2 == 0 else self.assertFalse
            assert_fun(self.gym.add_room(room[0], room[1]))

    def test_add_workout(self):
        self.assertTrue(self.gym.add_workout_class(self.workout1))
        self.assertFalse(self.gym.add_workout_class(self.workout1))
        workout3 = self.workout1
        workout4 = self.workout2
        self.assertFalse(self.gym.add_workout_class(workout3))
        self.assertTrue(self.gym.add_workout_class(self.workout2))
        self.assertFalse(self.gym.add_workout_class(self.workout2))
        self.assertFalse(self.gym.add_workout_class(workout4))

    def test_schedule_docstring(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(WorkoutClass('Boot Camp', ['Cardio 1']))
        self.gym.add_instructor(self.instructor1)
        self.instructor1.add_certificate("Cardio 1")
        self.assertTrue(
            self.gym.schedule_workout_class(
                datetime(
                    2019,
                    9,
                    9,
                    12,
                    0),
                "AC",
                "Boot Camp",
                1))

    def test_schedule_conflict_room(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(WorkoutClass('Boot Camp', ['Cardio 1']))
        self.gym.add_instructor(self.instructor1)
        self.instructor1.add_certificate("Cardio 1")
        self.assertTrue(
            self.gym.schedule_workout_class(
                datetime(
                    2019,
                    9,
                    9,
                    12,
                    0),
                "AC",
                "Boot Camp",
                1))
        self.assertFalse(
            self.gym.schedule_workout_class(
                datetime(
                    2019,
                    9,
                    9,
                    12,
                    0),
                "AC",
                "Boot Camp",
                1))

    def test_schedule_different_room(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(WorkoutClass('Boot Camp', ['Cardio 1']))
        self.gym.add_instructor(self.instructor1)
        self.instructor1.add_certificate("Cardio 1")
        self.assertTrue(
            self.gym.schedule_workout_class(
                datetime(
                    2019,
                    9,
                    9,
                    12,
                    0),
                "AC",
                "Boot Camp",
                1))
        self.gym.add_room("BA", 10)
        self.gym.add_instructor(self.instructor2)
        self.instructor2.add_certificate("Cardio 1")
        self.assertTrue(
            self.gym.schedule_workout_class(
                datetime(
                    2019,
                    9,
                    9,
                    12,
                    0),
                "BA",
                "Boot Camp",
                2))

    def test_schedule_no_certificate(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(self.workout2)
        self.gym.add_instructor(self.instructor1)
        self.assertFalse(
            self.gym.schedule_workout_class(
                datetime(
                    2019,
                    9,
                    9,
                    12,
                    0),
                "AC",
                "Intro to SE",
                1))

    def test_schedule_conflict_instructor(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(WorkoutClass('Boot Camp', ['Cardio 1']))
        self.gym.add_instructor(self.instructor1)
        self.instructor1.add_certificate("Cardio 1")
        self.assertTrue(
            self.gym.schedule_workout_class(
                datetime(
                    2019,
                    9,
                    9,
                    12,
                    0),
                "AC",
                "Boot Camp",
                1))
        self.gym.add_room("BA", 10)
        self.assertFalse(
            self.gym.schedule_workout_class(
                datetime(
                    2019,
                    9,
                    9,
                    12,
                    0),
                "BA",
                "Boot Camp",
                1))

    def test_register_docstring(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(WorkoutClass('Boot Camp', ['Cardio 1']))
        self.gym.add_instructor(self.instructor1)
        self.instructor1.add_certificate("Cardio 1")
        time_point = datetime(2019, 9, 9, 12, 0)
        self.assertTrue(
            self.gym.schedule_workout_class(
                time_point, "AC", "Boot Camp", 1))
        self.assertTrue(self.gym.register(time_point, "Gary", "Boot Camp"))
        self.assertFalse(self.gym.register(time_point, "Gary", "Boot Camp"))

    def test_register_conflict_time(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(WorkoutClass('Boot Camp', ['Cardio 1']))
        self.gym.add_instructor(self.instructor1)
        self.instructor1.add_certificate("Cardio 1")
        time_point = datetime(2019, 9, 9, 12, 0)
        self.gym.add_room("BA", 10)
        self.assertTrue(
            self.gym.schedule_workout_class(
                time_point, "AC", "Boot Camp", 1))
        self.assertTrue(self.gym.register(time_point, "Gary", "Boot Camp"))
        self.gym.add_room("BA", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_instructor(self.instructor2)
        self.assertTrue(
            self.gym.schedule_workout_class(
                time_point,
                "BA",
                "Intro to Com Sci",
                2))
        self.assertFalse(
            self.gym.register(
                time_point,
                "Gary",
                "Intro to Com Sci"))

    def test_register_over_capacity(self):
        self.gym.add_room("AC", 0)
        self.gym.add_workout_class(WorkoutClass('Boot Camp', ['Cardio 1']))
        self.gym.add_instructor(self.instructor1)
        self.instructor1.add_certificate("Cardio 1")
        time_point = datetime(2019, 9, 9, 12, 0)
        self.assertTrue(
            self.gym.schedule_workout_class(
                time_point, "AC", "Boot Camp", 1))
        self.assertFalse(self.gym.register(time_point, "Gary", "Boot Camp"))

    def test_register_multiple_room(self):
        self.gym.add_room("AC", 0)
        self.gym.add_workout_class(WorkoutClass('Boot Camp', ['Cardio 1']))
        self.gym.add_instructor(self.instructor1)
        self.instructor1.add_certificate("Cardio 1")
        time_point = datetime(2019, 9, 9, 12, 0)
        self.assertTrue(
            self.gym.schedule_workout_class(
                time_point, "AC", "Boot Camp", 1))
        self.gym.add_room("BA", 10)
        self.gym.add_instructor(self.instructor2)
        self.instructor2.add_certificate("Cardio 1")
        time_point = datetime(2019, 9, 9, 12, 0)
        self.assertTrue(
            self.gym.schedule_workout_class(
                time_point, "BA", "Boot Camp", 2))
        self.assertTrue(self.gym.register(time_point, "Gary", "Boot Camp"))

    def test_register_multiple_room_fail(self):
        self.gym.add_room("AC", 0)
        self.gym.add_workout_class(WorkoutClass('Boot Camp', ['Cardio 1']))
        self.gym.add_instructor(self.instructor1)
        self.instructor1.add_certificate("Cardio 1")
        time_point = datetime(2019, 9, 9, 12, 0)
        self.assertTrue(
            self.gym.schedule_workout_class(
                time_point, "AC", "Boot Camp", 1))
        self.gym.add_room("BA", 0)
        self.gym.add_instructor(self.instructor2)
        self.instructor2.add_certificate("Cardio 1")
        time_point = datetime(2019, 9, 9, 12, 0)
        self.assertTrue(
            self.gym.schedule_workout_class(
                time_point, "BA", "Boot Camp", 2))
        self.assertFalse(self.gym.register(time_point, "Gary", "Boot Camp"))

    def test_offer_docstring(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_instructor(self.instructor1)
        time_point = datetime(2019, 9, 9, 12, 0)
        self.gym.schedule_workout_class(
            time_point, "AC", "Intro to Com Sci", 1)
        exp = [("Diane", "Intro to Com Sci", "AC")]
        act = self.gym.offerings_at(time_point)
        self.assertListEqual(exp, act, self.msg(exp, act))

    def test_offer_empty(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_instructor(self.instructor1)
        time_point = datetime(2019, 9, 9, 12, 0)
        exp = []
        act = self.gym.offerings_at(time_point)
        self.assertListEqual(exp, act, self.msg(exp, act))

    def test_offer_multiple_instructor(self):
        self.gym.add_room("AC", 10)
        self.gym.add_room("BA", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_instructor(self.instructor1)
        self.gym.add_instructor(self.instructor2)
        time_point = datetime(2019, 9, 9, 12, 0)
        time_point2 = datetime(2019, 9, 9, 13, 0)
        self.gym.schedule_workout_class(
            time_point, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(
            time_point, "BA", "Intro to Com Sci", 2)
        exp = [("Diane", "Intro to Com Sci", "AC"),
               ("David", "Intro to Com Sci", "BA")]
        act = self.gym.offerings_at(time_point)
        self.assertCountEqual(
            exp,
            self.gym.offerings_at(time_point),
            self.msg(
                exp,
                act))
        self.assertListEqual(self.gym.offerings_at(
            time_point2), [], self.msg(exp, act))

    def test_offer_multiple_instructor2(self):
        self.gym.add_room("AC", 10)
        self.gym.add_room("BA", 10)
        self.gym.add_room("SS", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_workout_class(self.workout2)
        self.gym.add_workout_class(WorkoutClass("Intro to DB", []))
        self.gym.add_instructor(self.instructor1)
        self.gym.add_instructor(self.instructor2)
        self.instructor2.add_certificate("Intro to Com Sci")
        self.gym.add_instructor(Instructor(3, "Danny"))
        time_point = datetime(2019, 9, 9, 12, 0)
        time_point2 = datetime(2019, 9, 9, 13, 0)
        self.gym.schedule_workout_class(
            time_point, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(
            time_point, "BA", "Intro to Com Sci", 2)
        exp = [("Diane", "Intro to Com Sci", "AC"),
               ("David", "Intro to Com Sci", "BA")]
        act = self.gym.offerings_at(time_point)
        self.assertCountEqual(exp, act, self.msg(exp, act))
        self.gym.schedule_workout_class(
            time_point2, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(time_point2, "BA", "Intro to SE", 2)
        self.gym.schedule_workout_class(time_point2, "SS", "Intro to DB", 3)
        exp2 = [("Diane", "Intro to Com Sci", "AC"), ("David",
                                                      "Intro to SE", "BA"),
                ("Danny", "Intro to DB", "SS")]
        act2 = self.gym.offerings_at(time_point2)
        self.assertCountEqual(exp2, act2, self.msg(exp2, act2))

    def test_instructor_hour_docstring(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_instructor(self.instructor1)
        self.gym.add_instructor(self.instructor2)
        time_point = datetime(2019, 9, 9, 12, 0)
        time_point2 = datetime(2019, 9, 9, 13, 0)
        self.gym.schedule_workout_class(
            time_point, "AC", "Intro to Com Sci", 1)
        exp = {1: 1, 2: 0}
        act = self.gym.instructor_hours(time_point, time_point2)
        self.assertDictEqual(exp, act, self.msg(exp, act))

    def test_instructor_hour_no_work(self):
        self.gym.add_room("AC", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_instructor(self.instructor1)
        self.gym.add_instructor(self.instructor2)
        time_point = datetime(2019, 9, 9, 12, 0)
        time_point2 = datetime(2019, 9, 9, 13, 0)
        exp = {1: 0, 2: 0}
        act = self.gym.instructor_hours(time_point, time_point2)
        self.assertDictEqual(exp, act, self.msg(exp, act))

    def test_instructor_hour_multiple_working(self):
        self.gym.add_room("AC", 10)
        self.gym.add_room("BA", 10)
        self.gym.add_room("SS", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_workout_class(self.workout2)
        self.gym.add_workout_class(WorkoutClass("Intro to DB", []))
        self.gym.add_instructor(self.instructor1)
        self.gym.add_instructor(self.instructor2)
        self.instructor2.add_certificate("Intro to Com Sci")
        self.gym.add_instructor(Instructor(3, "Danny"))
        time_point = datetime(2019, 9, 9, 12, 0)
        time_point2 = datetime(2019, 9, 9, 13, 0)
        self.gym.schedule_workout_class(
            time_point, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(
            time_point, "BA", "Intro to Com Sci", 2)
        self.gym.schedule_workout_class(
            time_point2, "AC", "Intro to Com Sci", 1)
        exp = {1: 2, 2: 1, 3: 0}
        act = self.gym.instructor_hours(time_point, time_point2)
        self.assertDictEqual(exp, act, self.msg(exp, act))

    def test_instructor_hour_2(self):
        self.gym.add_room("AC", 10)
        self.gym.add_room("BA", 10)
        self.gym.add_room("SS", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_workout_class(self.workout2)
        self.gym.add_workout_class(WorkoutClass("Intro to DB", []))
        self.instructor1.add_certificate("Intro to DB")
        self.instructor1.add_certificate("Intro to DB")
        self.instructor1.add_certificate("Intro to Com Sci")
        self.instructor2.add_certificate("Intro to Com Sci")
        self.gym.add_instructor(self.instructor1)
        self.gym.add_instructor(self.instructor2)
        self.instructor2.add_certificate("Intro to Com Sci")
        self.gym.add_instructor(Instructor(3, "Danny"))
        time_point = datetime(2019, 9, 9, 12, 0)
        time_point2 = datetime(2019, 9, 9, 13, 0)
        time_point3 = datetime(2019, 9, 9, 14, 0)
        time_point4 = datetime(2019, 9, 9, 15, 0)
        time_point5 = datetime(2019, 9, 9, 16, 0)
        self.gym.schedule_workout_class(time_point, "SS", "Intro to DB", 3)
        self.gym.schedule_workout_class(
            time_point2, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(
            time_point3, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(
            time_point4, "BA", "Intro to Com Sci", 2)
        self.gym.schedule_workout_class(time_point5, "SS", "Intro to SE", 3)
        exp = {1: 2, 2: 1, 3: 0}
        act = self.gym.instructor_hours(time_point2, time_point4)
        self.assertDictEqual(exp, act, self.msg(exp, act))

    def test_payroll_one_hour(self):
        self.gym.add_room("AC", 10)
        self.gym.add_room("BA", 10)
        self.gym.add_workout_class(self.workout1)
        self.instructor1.add_certificate("Intro to DB")
        self.gym.add_instructor(self.instructor1)
        self.gym.add_instructor(self.instructor2)
        time_point = datetime(2019, 9, 9, 12, 0)
        time_point2 = datetime(2019, 9, 9, 13, 0)
        self.gym.schedule_workout_class(
            time_point, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(
            time_point, "BA", "Intro to Com Sci", 2)
        exp = [(1, "Diane", 1, 23.0), (2, "David", 1, 20.0)]
        act = self.gym.payroll(time_point, time_point2, 20.0)
        self.assertListEqual(exp, act, self.msg(exp, act))

    def test_payroll_multiple_hours(self):
        self.gym.add_room("AC", 10)
        self.gym.add_room("BA", 10)
        self.gym.add_room("SS", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_workout_class(self.workout2)
        self.gym.add_workout_class(WorkoutClass("Intro to DB", []))
        self.instructor1.add_certificate("Intro to DB")
        self.instructor1.add_certificate("Intro to DB")
        self.instructor1.add_certificate("Intro to Com Sci")
        self.instructor2.add_certificate("Intro to Com Sci")
        self.gym.add_instructor(self.instructor1)
        self.gym.add_instructor(self.instructor2)
        self.instructor2.add_certificate("Intro to Com Sci")
        self.gym.add_instructor(Instructor(3, "Danny"))
        time_point = datetime(2019, 9, 9, 12, 0)
        time_point2 = datetime(2019, 9, 9, 13, 0)
        self.gym.schedule_workout_class(
            time_point, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(
            time_point, "BA", "Intro to Com Sci", 2)
        self.gym.schedule_workout_class(
            time_point2, "AC", "Intro to Com Sci", 1)
        exp = [(1, "Diane", 2, 52.0),
               (2, "David", 1, 23.0), (3, "Danny", 0, 0.0)]
        act = self.gym.payroll(time_point, time_point2, 20.0)
        self.assertListEqual(exp, act, self.msg(exp, act))

    def test_payroll_multiple_hours2(self):
        self.gym.add_room("AC", 10)
        self.gym.add_room("BA", 10)
        self.gym.add_room("SS", 10)
        self.gym.add_workout_class(self.workout1)
        self.gym.add_workout_class(self.workout2)
        self.gym.add_workout_class(WorkoutClass("Intro to DB", []))
        self.instructor1.add_certificate("Intro to DB")
        self.instructor1.add_certificate("Intro to DB")
        self.instructor1.add_certificate("Intro to Com Sci")
        self.instructor2.add_certificate("Intro to Com Sci")
        self.gym.add_instructor(self.instructor1)
        self.gym.add_instructor(self.instructor2)
        self.instructor2.add_certificate("Intro to Com Sci")
        self.gym.add_instructor(Instructor(3, "Danny"))
        time_point = datetime(2019, 9, 9, 12, 0)
        time_point2 = datetime(2019, 9, 9, 13, 0)
        time_point3 = datetime(2019, 9, 9, 14, 0)
        time_point4 = datetime(2019, 9, 9, 15, 0)
        time_point5 = datetime(2019, 9, 9, 16, 0)
        self.gym.schedule_workout_class(time_point, "SS", "Intro to DB", 3)
        self.gym.schedule_workout_class(
            time_point2, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(
            time_point3, "AC", "Intro to Com Sci", 1)
        self.gym.schedule_workout_class(
            time_point4, "BA", "Intro to Com Sci", 2)
        self.gym.schedule_workout_class(time_point5, "SS", "Intro to SE", 3)
        exp = [(1, "Diane", 2, 52.0),
               (2, "David", 1, 23.0), (3, "Danny", 0, 0.0)]
        act = self.gym.payroll(time_point2, time_point4, 20.0)
        self.assertCountEqual(exp, act, self.msg(exp, act))


if __name__ == '__main__':
    unittest.main(exit=False)
