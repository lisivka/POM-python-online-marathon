"""
Write  the function check_positive(number) whose input parameter is a number.
The function checks whether the  set number is positive or negative:

in the case of a positive number the function should be displayed the corresponding message -
" You input positive number: input parameter of function";
in the case of a negative parameter the function should be raised the exception of your own class
MyError and displayed the corresponding message - "You input negative number: input parameter of function. Try again.";
in the case of incorrect data the function should be displayed the message - "Error type: ValueError!"
Function example:

check_positive (24)      #output:    "You input positive number: 24"
check_positive (-19)     #output:     "You input negative number: -19. Try again."
check_positive ("38")    #output:    "You input positive number: 38"
check_positive ("abc")  #output:     "Error type: ValueError!"
"""


class MyError(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"You input negative number: {float(self.number)}. Try again."


def check_positive(number):
    try:
        if float(number) > 0:
            return f"You input positive number: {float(number)}"
        elif float(number) < 0:
            raise MyError(number)
        else:
            return f"Error type: ValueError!"
    except MyError as e:
        return e

    except (TypeError, ValueError):
        return f"Error type: ValueError!"


if __name__ == "__main__":
    # print(check_positive(0))
    # print(check_positive(24))

    print(check_positive(8.9))
    # You input positive number: 8.9
    print(check_positive(-19))
    # You input negative number: -19.0. Try again.
    print(check_positive(0.7))
    # You input positive number: 0.7
    print(check_positive(-0.6))
    # You input negative number: -0.6. Try again.
    print(check_positive("abs"))
    # Error type: ValueError!
    print(check_positive("45"))
    # You input positive number: 45.0
    print(check_positive("-235"))
    # You input negative number: -235.0. Try again.
