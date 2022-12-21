"""
Create function create_account(user_name: string,
password: string, secret_words: list).
This function should return inner function check.

The function check compares the values of its
arguments with password and secret_words:
the password must match completely, secret_words may be misspelled (just one element).

Password should contain at least 6 symbols including
one uppercase letter, one lowercase letter,
special character and one number.

Otherwise function create_account raises ValueError.

For example:
tom = create_account("Tom", "Qwerty1", ["1", "word"]) raises Value error

If tom = create_account("Tom", "Qwerty1_", ["1", "word"])
then
tom("Qwerty1_",  ["1", "word"]) return True
tom("Qwerty1_",  ["word"]) return False due to different length of   ["1", "word"] and  ["word"]
tom("Qwerty1_",  ["word", "12"]) return True
tom("Qwerty1!",  ["word", "1"]) return False because "Qwerty1!" not equals to "Qwerty1_"
"""


def create_account(user_name: str, password: str, secret_words: list):
    def check(password_check: str, secret_words_check: list):
        return check


if __name__ == '__main__':
    tom = create_account("Tom", "Qwerty1_", ["1", "word"])
    check1 = tom("Qwerty1_", ["1", "word"])
    check2 = tom("Qwerty1_", ["word"])
    check3 = tom("Qwerty1_", ["word", "2"])
    check4 = tom("Qwerty1!", ["word", "12"])


    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_1_true))
