"""Write  the function day_of_week(day) whose input parameter is a number or string representation of number. 
The function returns the corresponding day of the week if the input parameter is in the range of 1 to 7, namely

· in the case when the input parameter is 5 the function should be displayed the message – "Friday"
· in the case when the input parameter is not in the range of 1 to 7 the function should be displayed the message – 
    "There is no such day of the week! Please try again."
· in the case of incorrect data the function should be displayed the message - 
    "You did not enter a number! Please try again."

Note: in the function you must use the "try except" construct.


Function example:
day_of_week(2)                     # output:   "Tuesday"
day_of_week(11)                     # output:  "There is no such day of the week! Please try again."
day_of_week("Monday")       # output:   "You did not enter a number! Please try again."""


def day_of_week(day: int):
    try:
        week = [None,
                "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", ]
        if 1 <= int(day) <= 7:
            return week[int(day)]
        else:
            return f"There is no such day of the week! Please try again."
    except (TypeError, ValueError):
        return f"You did not enter a number! Please try again."


if __name__ == "__main__":
    print(day_of_week(2))

    print(day_of_week(5))
    # Friday

    print(day_of_week(1))
    # Monday

    print(day_of_week(0))
    # There is no such day of the week! Please try again.

    print(day_of_week(-9))
    # There is no such day of the week! Please try again.

    print(day_of_week("Sunday"))
    # You did not enter a number! Please try again.

    print(day_of_week("6"))
    # Saturday

    print(day_of_week("9"))
    # There is no such day of the week! Please try again.
    print(day_of_week(10 / 2))
    print(day_of_week("5"))
    print(day_of_week("5.1"))
