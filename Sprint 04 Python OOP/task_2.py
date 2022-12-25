"""
https://softserve.academy/mod/quiz/attempt.php?attempt=362653&cmid=10824&page=1#

Create a Pizza class with the attributes order_number and ingredients (which is given as a list).
 Only the ingredients will be given as input.

You should also make it so that its possible to choose a ready made pizza flavour
rather than typing out the ingredients manually!
As well as creating this Pizza class, hard-code the following pizza flavours.

Создайте класс Pizza с атрибутами номер_заказа и ингредиенты (которые представлены в виде списка).
Только ингредиенты будут даны в качестве входных данных.

Вы также должны сделать так, чтобы можно было выбрать вкус готовой пиццы, а не вводить ингредиенты вручную!
Помимо создания этого класса Pizza, жестко закодируйте следующие вкусы пиццы.
img.png

Examples:
p1 = Pizza(["bacon", "parmesan", "ham"])   # order 1
p2 = Pizza.garden_feast()                  # order 2
p1.ingredients ➞ ["bacon", "parmesan", "ham"]
p2.ingredients ➞ ["spinach", "olives", "mushroom"]
p1.order_number ➞ 1
p2.order_number ➞ 2
"""


class Pizza:
    orders = 0

    def __init__(self, ingredients: list):
        Pizza.orders += 1
        self.order_number = Pizza.orders
        self.ingredients = ingredients

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])


if __name__ == "__main__":
    p1 = Pizza(['bacon', 'parmesan', 'ham'])
    print(p1.ingredients)
    # ['bacon', 'parmesan', 'ham']
    # ['bacon', 'parmesan', 'ham']
    p2 = Pizza.garden_feast()
    print(p2.ingredients)
    # ['spinach', 'olives', 'mushroom']
    # ['spinach', 'olives', 'mushroom']
    p3 = Pizza.hawaiian()
    print(p3.ingredients)
    # ['ham', 'pineapple']
    # ['ham', 'pineapple']
    p4 = Pizza.meat_festival()
    print(p4.ingredients)
    # ['beef', 'meatball', 'bacon']
    # ['beef', 'meatball', 'bacon']
    p5 = Pizza(["pepperoni", "bacon"])
    print(p5.ingredients)
    # ['pepperoni', 'bacon']
    # ['pepperoni', 'bacon']
    my_pizza = Pizza(['cheese', 'caviar', 'oyster', 'uranium'])
    print(my_pizza.ingredients)
    # ['cheese', 'caviar', 'oyster', 'uranium']
    # ['cheese', 'caviar', 'oyster', 'uranium']
    print(p1.order_number)
    print(p2.order_number)
    print(p3.order_number)
    print(p4.order_number)
    print(p5.order_number)
    print(my_pizza.order_number)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
