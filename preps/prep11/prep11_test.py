import prep11 as p11
import unittest
import random
import timeit


class TestMergeSort(unittest.TestCase):
    def test_ascending(self):
        arg = [1, 2, 3, 4, 5, 6]
        exp = [1, 2, 3, 4, 5, 6]
        actual = p11.mergesort3(arg)
        self.assertEqual(actual, exp)

    def test_descending(self):
        arg = [6, 5, 4, 3, 2, 1]
        exp = [1, 2, 3, 4, 5, 6]
        act = p11.mergesort3(arg)
        self.assertEqual(act, exp)

    def test_base_case1(self):
        arg = [1]
        exp = [1]
        act = p11.mergesort3(arg)
        self.assertEqual(act, exp)

    def test_base_case2(self):
        arg = [2, 1]
        exp = [1, 2]
        act = p11.mergesort3(arg)
        self.assertEqual(act, exp)

    def test_average(self):
        arg = [2, 1, 4, 3, 6, 5]
        exp = sorted(arg)
        act = p11.mergesort3(arg)
        self.assertEqual(act, exp)

    def test_random(self):
        arg = random.sample([k for k in range(10)], 5)
        exp = sorted(arg)
        act = p11.mergesort3(arg)
        self.assertEqual(act, exp)

    def test_random_duplicate(self):
        arg = [random.randint(1, 10) for k in range(11)]
        exp = sorted(arg)
        act = p11.mergesort3(arg)
        self.assertEqual(act, exp)

    def test_worst_case_time(self):
        arg = [i for i in range(10000, 0, -1)]
        beg = timeit.default_timer()
        exp = sorted(arg)
        finish = timeit.default_timer()
        print(finish - beg)
        res = []
        for i in range(20):
            start = timeit.default_timer()
            act = p11.mergesort3(arg)
            end = timeit.default_timer()
            res.append(end - start)
            print("Execution time: " + str(end - start))
        print("Maximum execution time: " + str(max(res)))
        print("Minimum execution time: " + str(min(res)))
        self.assertEqual(act, exp)
        self.assertEqual(end - start < 2.5, True, "You should make your program finish in 5 seconds")


class TestKth(unittest.TestCase):
    def test_min(self):
        arg = random.sample([k for k in range(10)], 7)
        exp = min(arg)
        act = p11.kth_smallest(arg, 0)
        self.assertEqual(act, exp)

    def test_max(self):
        arg = random.sample([k for k in range(10)], 7)
        exp = max(arg)
        act = p11.kth_smallest(arg, len(arg) - 1)
        self.assertEqual(act, exp)

    def test_left(self):
        arg = random.sample([k for k in range(10)], 7)
        exp = sorted(arg)[2]
        act = p11.kth_smallest(arg, 2)
        self.assertEqual(act, exp)

    def test_pivot(self):
        arg = random.sample([k for k in range(10)], 7)
        exp = sorted(arg)[4]
        act = p11.kth_smallest(arg, 4)
        self.assertEqual(act, exp)

    def test_right(self):
        arg = random.sample([k for k in range(10)], 7)
        exp = sorted(arg)[5]
        act = p11.kth_smallest(arg, 5)
        self.assertEqual(act, exp)

    def test_error_1(self):
        arg = random.sample([k for k in range(10)], 7)
        exp = -1
        try:
            act = p11.kth_smallest(arg, -1)
        except IndexError:
            act = -1
        self.assertEqual(act, exp)

    def test_error_2(self):
        arg = random.sample([k for k in range(10)], 7)
        exp = -1
        try:
            act = p11.kth_smallest(arg, 10)
        except IndexError:
            act = -1
        self.assertEqual(act, exp)


if __name__ == "__main__":
    unittest.main(exit=False)
