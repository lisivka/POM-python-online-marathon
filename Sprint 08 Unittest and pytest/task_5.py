"""
Create class Worker with fields name and salary. If salary negative raise ValueError

Create a method get_tax_value() that calculate tax from salary .
Tax must be calculate like "progressive tax" with next step:

less then 1000 - 0%
1001 - 3000 - 10%
3001 - 5000 - 15%
5001 - 10000 - 21%
10001 - 20000 - 30%
20001 - 50000 - 40%
more than 50000 - 47%
Please create WorkerTest class with unitest to the class Worker.
Try to use setUp and tearDown methods. Don`t use assertRaises in tests.
"""

import unittest


class Worker:
    tax_levels = {
        (0, 1000): [0, 0],
        (1000, 3000): [10, 0],
        (3000, 5000): [15, 200],
        (5000, 10000): [21, 300 + 200],
        (10000, 20000): [30, 1050 + 300 + 200],
        (20000, 50000): [40, 3000 + 1050 + 300 + 200],
        (50000, 10 ** 100): [47, 12000 + 3000 + 1050 + 300 + 200],
    }

    def __init__(self, name, salary=None):
        self.name = name
        if salary is None:
            self.salary = 0
        elif salary < 0:
            raise ValueError
        else:
            self.salary = salary

    def salary(self):
        return self.salary

    def get_tax_value(self) -> int:
        salary = self.salary
        levels = tuple(Worker.tax_levels.keys())
        tax_rates = Worker.tax_levels
        for limit in levels:
            percent, tax_base = tax_rates[limit]
            if limit[0] <= salary <= limit[1]:
                tax = (salary - limit[0]) * percent / 100 + tax_base
            else: tax=0
        return float(tax)


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Misha", 100000)

    def test_salary_property(self):
        self.assertEqual(self.worker.salary, 100000)

    def test_get_tax_value(self):
        self.assertEqual(self.worker.get_tax_value(), 40050.0)

    @unittest.expectedFailure
    def test_raises(self):
        self.worker.salary = -1000
        self.assertRaises(self.test_get_tax_value())

    def test_Natasha(self):
        worker = Worker("Natasha", 1001)
        print(worker.get_tax_value(), 0.1)
    def tearDown(self) -> None:
        self.worker = None


if __name__ == '__main__':
    # print(expectedFailures)
    # 1
    # 0
    print("=======================")
    worker = Worker("Vasia")
    print(worker.get_tax_value())
    # # 0.0
    print("=======================")
    worker = Worker("Petia", 1000)
    print(worker.get_tax_value())
    # 0.0
    # print("=======================")
    worker = Worker("Natasha", 1001)
    print(worker.get_tax_value())
    # # 0.1
    # print("=======================")
    worker = Worker("Vika", 100000)
    print(worker.get_tax_value())
    # # 40050.0
