"""
Write the programm that calculate total price with discount by the products.
Use class Product(name, price, count) and class Cart. In class Cart you can add the products.
Discount depends on count product:
count	discount
at least 5	5%
at least 7	10%
at least 10	20%
at least 20	30%
more than 20	50%
Write unittest with class CartTest and test all methods with logic
"""

import unittest


class Product:
    def __init__(self, name: str, price: float, count: int):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, products: tuple):
        self.products = products

    def get_total_price(self) -> float:
        total_price = 0
        for product in self.products:
            price_discount = product.price * (1 - self.get_discount(product.count) / 100)
            total_price += product.count * price_discount
        return total_price

    @staticmethod
    def get_discount(count: int) -> int:
        discount = 0
        if count > 20:       discount = 50
        if count == 20:      discount = 30
        if 20 > count >= 10: discount = 20
        if 10 > count >= 7:  discount = 10
        if 7 > count >= 5:   discount = 5
        return discount


class CartTest(unittest.TestCase):
    products = (Product('p1', 10, 4),
                Product('p2', 100, 5),
                Product('p3', 200, 6),
                Product('p4', 300, 7),
                Product('p5', 400, 9),
                Product('p6', 500, 10),
                Product('p7', 1000, 20))
    cart = Cart(products)

    def test_discounted_price(self):
        expected = 24785.0
        actual = self.cart.get_total_price()
        self.assertEqual(actual, expected)

    def test_get_discount_50(self):
        expected = 50
        actual = self.cart.get_discount(25)
        self.assertEqual(actual, expected)

    def test_get_discount_30(self):
        expected = 30
        actual = self.cart.get_discount(20)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # print(count_tests > 0)
    # # True
    # # False
    # print(failures)
    # # 0
    # # 0
    # print(errors)
    # # 0
    # # 0
    # print(assertEqual)
    # # True
    # # False
    # products = (Product('p1', 10, 4),
    #             Product('p2', 100, 5),
    #             Product('p3', 200, 6),
    #             Product('p4', 300, 7),
    #             Product('p5', 400, 9),
    #             Product('p6', 500, 10),
    #             Product('p7', 1000, 20))
    # # print(products)
    # cart = Cart(products)
    # print(cart.get_total_price())
    # 24785.0
