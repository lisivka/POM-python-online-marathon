"""
Write  the function check_odd_even (number) whose input parameter is an integer number.
The function checks whether the  set number is even or odd:

in the case of an even number the function should be displayed the corresponding message - "Entered number is even";
in the case of an odd number the function should be displayed the corresponding message -  "Entered number is odd";
in the case of incorrect data the function should be displayed the message - "You entered not a number."
Note: in the function you must use the "try except" construct.

Function example:
check_odd_even (24)     #output:    "Entered number is even"
check_odd_even (19)     #output:     "Entered number is odd"
"""


def check_odd_even(number: int) -> str:
    try:
        return "Entered number is even" if number % 2 == 0 else "Entered number is odd"
    except (ValueError, TypeError):
        return "You entered not a number."


if __name__ == "__main__":
    print(check_odd_even(15))
    # Entered number is odd

    print(check_odd_even(-6))
    # Entered number is even

    print(check_odd_even(0))
    # Entered number is even

    print(check_odd_even("plp"))
    # You entered not a number.

    print(check_odd_even(36))
    # Entered number is even

    print(check_odd_even('36'))
    print(check_odd_even([36]))
