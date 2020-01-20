from prep3 import *
import unittest


class test_salaried_employee(unittest.TestCase):
    def test_one_month(self):
        a = SalariedEmployee(1, "b", 6000)
        a.pay(date(2018, 1, 28))
        expect = 500
        actual = a.total_pay()
        self.assertEqual(expect, actual, "The employee has one moth payment")

    def test_two_months(self):
        b = SalariedEmployee(2, "c", 12000)
        b.pay(date(2018, 2, 28))
        b.pay(date(2018, 3, 28))
        expect = 2000
        actual = b.total_pay()
        self.assertEqual(
            expect,
            actual,
            "The employee has two months payment")


class test_hour_salaried(unittest.TestCase):
    def test_one_month(self):
        a = HourlyEmployee(3, "d", 10, 50)
        a.pay(date(2018, 4, 28))
        expect = 500
        actual = a.total_pay()
        self.assertEqual(expect, actual, "The hour employee only payed once")

    def test_two_months(self):
        b = HourlyEmployee(4, "c", 20, 50)
        b.pay(date(2018, 5, 28))
        b.pay(date(2018, 6, 28))
        expect = 2000
        actual = b.total_pay()
        self.assertEqual(expect, actual, "The hour employee has payed twice")


class test_total_payroll(unittest.TestCase):
    def test_one_salaried_employee_1(self):
        a = Company([SalariedEmployee(5, "b", 24000)])
        a.pay_all(date(2018, 7, 28))
        expect = 2000
        actual = a.total_payroll()
        self.assertEqual(
            expect,
            actual,
            "There is a salaried employee paied 2000")

    def test_one_salaried_employee_2(self):
        a = Company([SalariedEmployee(5, "b", 36000)])
        a.pay_all(date(2018, 8, 28))
        a.pay_all((date(2018, 9, 28)))
        expect = 6000
        actual = a.total_payroll()
        self.assertEqual(
            expect,
            actual,
            "There is a salaried employee paied 6000")

    def test_one_hourly_employee(self):
        b = Company([HourlyEmployee(6, "c", 20, 30)])
        b.pay_all(date(2018, 10, 28))
        expect = 600
        actual = b.total_payroll()
        self.assertEqual(
            expect,
            actual,
            "There is a hourly emplyee paied 600")

    def test_one_hourly_employee_2(self):
        b = Company([HourlyEmployee(6, "c", 10, 50)])
        b.pay_all(date(2018, 11, 28))
        b.pay_all(date(2018, 12, 28))
        expect = 1000
        actual = b.total_payroll()
        self.assertEqual(
            expect,
            actual,
            "There is a hourly employee paied 1000")

    def test_mixed_employee(self):
        c = Company([SalariedEmployee(4, "a", 12000),
                     HourlyEmployee(5, "b", 20, 50)])
        c.pay_all(date(2019, 1, 28))
        expect = 2000
        actual = c.total_payroll()
        self.assertEqual(
            expect,
            actual,
            "There is a salaried employee and a hourly employee")

    def test_mixed_employee_2(self):
        c = Company([SalariedEmployee(5, "b", 12000),
                     HourlyEmployee(6, "c", 20, 50)])
        c.pay_all(date(2019, 2, 28))
        c.pay_all(date(2019, 3, 28))
        expect = 4000
        actual = c.total_payroll()
        self.assertEqual(
            expect,
            actual,
            "There is a salaried employee and a hourly employee paid twice")


if __name__ == "__main__":
    unittest.main(exit=False)
