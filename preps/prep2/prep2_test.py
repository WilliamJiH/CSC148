from prep2 import Spinner
import unittest


class Initializertest(unittest.TestCase):
    def test_OneSlot(self):
        sample = Spinner(1)
        self.expected_slots = 1
        self.expected_position = 0
        actual_slots = sample.slots
        actual_position = sample.position
        self.assertEqual(actual_slots, self.expected_slots, "The slots is 1")
        self.assertEqual(actual_position, self.expected_position,
                         "The pos starts 0")

    def test_BiggerSlot(self):
        sample = Spinner(5)
        expected_slots = 5
        expected_pos = 0
        actual_slots = sample.slots
        actual_pos = sample.position
        self.assertEqual(actual_slots, expected_slots, "There are 5 slots")
        self.assertEqual(actual_pos, expected_pos, "The pos starts at 0")


class Spintest(unittest.TestCase):
    def test_Oneslot(self):
        sample = Spinner(1)
        sample.spin(1)
        actual_pos = sample.position
        expected_pos = 0
        self.assertEqual(actual_pos, expected_pos, "The pos always at 0")

    def test_OneMove(self):
        sample = Spinner(5)
        sample.spin(1)
        actual_pos = sample.position
        expected_pos = 1
        self.assertEqual(actual_pos, expected_pos, "The pos moves to 1")

    def test_InnerMove(self):
        sample = Spinner(5)
        sample.spin(3)
        second_pos = sample.position
        expected_pos = 3
        self.assertEqual(second_pos, expected_pos, "The pos moves to 3")

    def test_BackMove(self):
        sample = Spinner(5)
        sample.spin(5)
        third_pos = sample.position
        expected_pos = 0
        self.assertEqual(third_pos, expected_pos, "The pos moves back to 0")

    def test_OverMove(self):
        sample = Spinner(5)
        sample.spin(6)
        actual_pos = sample.position
        expected_pos = 1
        self.assertEqual(actual_pos, expected_pos, "The pos over move by 1")


if __name__ == "__main__":
    unittest.main(exit=False)
