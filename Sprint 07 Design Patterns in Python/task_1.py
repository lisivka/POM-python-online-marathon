"""
You have to create a main course and a dessert at an Italian and a French restaurant,
but you won't mix one cuisine with the other.
Your task is:
1) define a class Product with an abstract method cook(). This class would be base class for the next classes:

- class FettuccineAlfredo with field name ("Fettuccine Alfredo"),
    method cook() provides an output of the formatted string "Italian main course prepared: " and name of the dish;

- class Tiramisu, with field name ("Tiramisu"),
    method cook() provides an output of the formatted string "Italian dessert prepared:" and name of the dish;

- class DuckALOrange, with field name ("Duck À L'Orange"),
    method cook() provides an output of the formatted string "French main course prepared: " and name of the dish;

- class CremeBrulee,  with field name ("Crème brûlée"),
    method cook() provides an output of the formatted string "French dessert prepared: " and name of the dish.

2) define a class Factory with an abstract method get_dish() that takes  type_of_meal as a parameter.
This class would be base class for the classes ItalianDishesFactory and FrenchDishesFactory.
The method get_dish() according to type_of_meal ("main" or "dessert") invokes the dish of appropriate cousine;

+ 3) define a class FactoryProducer with the method get_factory().
The method takes the parameter type_of_factory
and invokes the appropriate dishes factory (classes ItalianDishesFactory or FrenchDishesFactory).
"""
# https://stackabuse.com/creational-design-patterns-in-python/


from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    name = "Fettuccine Alfredo"

    def cook(self):
        print(f"Italian main course prepared: {self.name}")


class Tiramisu(Product):
    name = "Tiramisu"

    def cook(self):
        print(f"Italian dessert prepared: {self.name}")


class DuckALOrange(Product):
    name = "Duck À L'Orange"

    def cook(self):
        print(f"French main course prepared: {self.name}")


class CremeBrulee(Product):
    name = "Crème brûlée"

    def cook(self):
        print(f"French dessert prepared: {self.name}")


class Factory(ABC):
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class FactoryProducer:
    def get_factory(self, type_of_factory: str):
        if type_of_factory == "italian": return ItalianDishesFactory()
        if type_of_factory == "french": return FrenchDishesFactory()


class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal: str):
        if type_of_meal == "main": return FettuccineAlfredo()
        if type_of_meal == "dessert": return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal: str):
        if type_of_meal == "main": return DuckALOrange()
        if type_of_meal == "dessert": return CremeBrulee()


if __name__ == "__main__":
    # https://stackabuse.com/creational-design-patterns-in-python/ !!!

    fp = FactoryProducer()
    # print(fp)
    fac = fp.get_factory("italian")
    main_dish = fac.get_dish("main")
    # print(main_dish)
    main_dish.cook()
    # Italian main course prepared: Fettuccine Alfredo
    print("==========================")

    dessert = fac.get_dish("dessert")
    dessert.cook()
    # Italian dessert prepared: Tiramisu

    print("==========================")
    fac1 = fp.get_factory("french")
    main_dish = fac1.get_dish("main")
    main_dish.cook()
    # French main course prepared: Duck À L'Orange

    print("==========================")
    dessert = fac1.get_dish("dessert")
    dessert.cook()
    # French dessert prepared: Crème brûlée

    print(dessert.__dict__)
