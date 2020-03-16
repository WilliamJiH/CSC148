from prep10 import *
import unittest


class TestBool(unittest.TestCase):
    def test_basic(self):
        arg = Bool(True)
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_basic_2(self):
        arg = Bool(False)
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)


class TestBoolOp(unittest.TestCase):
    def test_basic_op(self):
        arg = BoolOp("and", [Bool(True), Bool(True)])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_basic_op_2(self):
        arg = BoolOp("and", [Bool(True), Bool(False)])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)

    def test_basic_op_3(self):
        arg = BoolOp("and", [Bool(False), Bool(False)])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)

    def test_basic_op_4(self):
        arg = BoolOp("or", [Bool(True), Bool(True)])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_basic_op_5(self):
        arg = BoolOp("or", [Bool(True), Bool(False)])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_basic_op_6(self):
        arg = BoolOp("or", [Bool(False), Bool(False)])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)

    def test_complex_1(self):
        arg = BoolOp("or",
                     [Bool(False), BoolOp("and", [Bool(True), Bool(False)])])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)

    def test_complex_2(self):
        arg = BoolOp("and", [Bool(True), Bool(False),
                             BoolOp("or", [Bool(True), Bool(False)])])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)

    def test_complex_3(self):
        arg = BoolOp("or", [BoolOp("or", [Bool(True), Bool(False)]),
                            BoolOp("and", [Bool(False), Bool(False)])])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_complex_4(self):
        arg = BoolOp("and",
                     [BoolOp("or", [BoolOp("and", [Bool(True), Bool(True)])])])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_complex_5(self):
        arg = BoolOp("or", [BoolOp("and", [Bool(False), BoolOp("or",
                                                               [Bool(True),
                                                                Bool(False)])]),
                            BoolOp("or", [Bool(False), Bool(False)]),
                            Bool(False)])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)

    def test_complex_6(self):
        arg = BoolOp("or", [BoolOp("or", [Bool(False), BoolOp("or",
                                                              [Bool(True),
                                                               Bool(False)])]),
                            BoolOp("or", [Bool(False), Bool(False)]),
                            Bool(False)])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)


class TestCompare(unittest.TestCase):
    def test_basic_comp_1(self):
        arg = Compare(Num(1), [("<", Num(2))])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_basic_comp_2(self):
        arg = Compare(Num(2), [("<=", Num(2))])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_basic_comp_3(self):
        arg = Compare(Num(2), [("<", Num(2))])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)

    def test_complex_comp_1(self):
        arg = Compare(Num(1), [("<", Num(2)), ("<=", Num(2)), ("<", Num(3))])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_complex_comp_2(self):
        arg = Compare(Num(1), [("<", Num(2)), ("<=", Num(3)), ("<", Num(2.5))])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)

    def test_complex_comp_3(self):
        arg = Compare(Num(1), [
            ("<", Num(int(BoolOp("or", [Num(1), Num(2)]).evaluate())))])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)

    def test_complex_comp_4(self):
        arg = Compare(Num(0), [
            ("<=", Num(int(Compare(Num(2), [("<", Num(2))]).evaluate())))])
        actual = arg.evaluate()
        expect = True
        self.assertEqual(expect, actual)

    def test_complex_comp_5(self):
        arg = Compare(Num(0), [("<=", Num(3)), ("<", Num(1))])
        actual = arg.evaluate()
        expect = False
        self.assertEqual(expect, actual)


if __name__ == "__main__":
    unittest.main(exit=False)
