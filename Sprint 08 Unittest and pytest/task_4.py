"""
Create class Triangle with method get_area() that calculate area of triangle. As input you will have list of 3 sides size
Examples:
triangle = Triangle([3, 3, 3])
Use classes TriangleNotValidArgumentException and TriangleNotExistException
Create class TriangleTest with unittest and subTest() context manager for class Triangle.
test data:
valid_test_data = [
    ((3, 4, 5), 6.0),
    ((10, 10, 10), 43.30),
    ((6, 7, 8), 20.33),
    ((7, 7, 7), 21.21),
    ((50, 50, 75), 1240.19),
    ((37, 43, 22), 406.99),
    ((26, 25, 3), 36.0),
    ((30, 29, 5), 72.0),
    ((87, 55, 34), 396.0),
    ((120, 109, 13), 396.0),
    ((123, 122, 5), 300.0)
]
not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    (7, "str", 7),
    ('1', '1', '1'),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    'str',
    10,
    ('a', 'str', 7)
]

"""

import unittest


class TriangleNotValidArgumentException(Exception):
    def __init__(self, message="Not valid arguments"):
        self.message = message

    def __str__(self):
        return self.message


class TriangleNotExistException(Exception):

    def __init__(self, message="Can`t create triangle with this arguments"):
        self.message = message

    def __str__(self):
        return self.message


class Triangle:
    def __init__(self, sides: tuple):
        if self.check_not_valid_arg(sides) and self.check_not_exist_triangle(sides):
            self.sides = sides
            # self.area = self.get_area()
            self.get_area()

    def check_not_valid_arg(self, sides):
        if not isinstance(sides, (list, tuple)) or len(sides) != 3:
            raise TriangleNotValidArgumentException
        for side in sides:
            if not isinstance(side, (int, float)):
                raise TriangleNotValidArgumentException
        else:
            return True

    def check_not_exist_triangle(self, sides):
        a, b, c = sides
        if any((a <= 0, b <= 0, c <= 0, a + b <= c, b + c <= a, c + a <= b)):
            raise TriangleNotExistException
        else:
            return True

    def get_area(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        self.area = round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 1)

        return self.area


class TriangleTest(unittest.TestCase):
    def setUp(self):
        self.valid_test_data = [
            ((3, 4, 5), 6.0),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        self.not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        self.not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]

    def test_area_for_valid_data(self):
        for item in self.valid_test_data:
            with self.subTest(item=item):
                triange = Triangle(item[0])
                self.assertEqual(triange.get_area(), item[1])

    def test_not_valid_triangle(self):
        for item in self.not_valid_triangle:
            with self.subTest(item=item):
                self.assertRaises(TriangleNotExistException, Triangle, item)

    def test_exception(self):
        for item in self.not_valid_arguments:
            with self.subTest(item=item):
                self.assertRaises(TriangleNotValidArgumentException, Triangle, item)

    def tearDown(self):
        self.not_valid_arguments = None
        self.not_valid_triangle = None
        self.valid_test_data = None


if __name__ == '__main__':
    not_valid_triangle = [
        (1, 2, 3),
        (1, 1, 2),
        (7, 7, 15),
        (100, 7, 90),
        (17, 18, 35),
        (127, 17, 33),
        (145, 166, 700),
        (1000, 2000, 1),
        (717, 17, 7),
        (0, 7, 7),
        (-7, 7, 7)
    ]
    for data in not_valid_triangle:
        try:
            Triangle(data)
            # print("Triangle", data)
        except TriangleNotExistException as e:
            print(e)
    # Can`t create triangle with this arguments

    print("========================")
    valid_test_data = [
        (3, 4, 5),
        (26, 25, 3),
        (30, 29, 5),
        (87, 55, 34),
        (120, 109, 13),
        (123, 122, 5)
    ]
    for data in valid_test_data:
        print(Triangle(data).get_area())
        #
        # 6.0
        # 36.0
        # 72.0
        # 396.0
        # 396.0
        # 300.0

    print("========================")
    not_valid_arguments = [
        ('3', 4, 5),
        ('a', 2, 3),
        'string',
        (7, 2),
        (7, 7, 7, 7),
        10
    ]
    for data in not_valid_arguments:
        try:
            Triangle(data)
        except TriangleNotValidArgumentException as e:
            print(e)
