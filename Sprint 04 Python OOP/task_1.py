"""
Define a class Employee. In the class Employee implement the instance attributes as firstname, lastname and salary.

Create the static method from_string() which parses a string containing these attributes and assigns
them to the correct properties. Properties will be separated by a dash.

Examples:
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
emp1.firstname ➞ "Mary"
emp1.salary ➞ 60000
emp2.firstname ➞ "John"
"""
import inspect


class Employee:

    def __init__(self, firstname, lastname: object, salary: object):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(string: str):
        firstname, lastname, salary = string.split("-")
        return Employee(firstname, lastname, int(salary))


if __name__ == "__main__":
    emp1 = Employee("Mary", "Sue", 60000)
    emp2 = Employee.from_string("John-Smith-55000")
    print(emp1.firstname)  # "Mary"
    print(emp1.salary)  # 60000
    print(emp2.firstname)  # "John"
    print(emp2.salary)

    print("======================")

    # emp1 = Employee("Mary", "Sue", 60000)
    # print(emp1.firstname)
    # print(emp1.lastname)
    # print(emp1.salary)
    # print(isinstance(emp1.salary, int))
    # Mary
    # Sue
    # 60000
    # True
    # Mary
    # Sue
    # 60000
    # True
    # emp2 = Employee.from_string("John-Smith-55000")
    # print(emp2.firstname)
    # print(emp2.lastname)
    # print(emp2.salary)
    # print(isinstance(emp2.salary, int))
    # John
    # Smith
    # 55000
    # True
    # John
    # Smith
    # 55000
    # True
    # emp3 = Employee.from_string("Susan-Walker-70000")
    # print(emp3.firstname)
    # print(emp3.lastname)
    # print(emp3.salary)
    # Susan
    # Walker
    # 70000
    # Susan
    # Walker
    # 70000
    # emp4 = Employee.from_string("Michael-Ferry-90000")
    # print(emp4.firstname)
    # print(emp4.lastname)
    # print(emp4.salary)
    # Michael
    # Ferry
    # 90000
    # Michael
    # Ferry
    # 90000
    # emp5 = Employee("Graham", "Derrell", 55000)
    # print(emp5.firstname)
    # print(emp5.lastname)
    # print(emp5.salary)
    # Graham
    # Derrell
    # 55000
    # Graham
    # Derrell
    # 55000
    # import inspect
    #
    print(isinstance(inspect.getattr_static(Employee, "from_string"), staticmethod))
    # True
    # False
    print(inspect.getattr_static(Employee, "from_string"))
