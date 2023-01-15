"""
You have function divide
def divide(num1, num2):
    return float(n

Please, write the code with unit tests for the function "divide":
minimum 3 tests
must chek all flows
all test must be pass
no failures
no skip


"""


def divide(num_1, num_2):
    return float(num_1) / num_2


import unittest


class DivideTest(unittest.TestCase):
    def test_zero_division(self):
        self.assertRaises(Exception, divide, 3, 0)

    def test_divide(self):
        expected = 5
        actual = divide(30,6)
        self.assertEqual(actual, expected)

    def test_str(self):
        expected = 5
        actual = divide("30",6)
        self.assertEqual(actual, expected)

    def test_type_error(self):
        self.assertRaises(Exception, divide, 30, "5")
