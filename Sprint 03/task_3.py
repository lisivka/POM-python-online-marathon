"""
Create function create_account(user_name: string,password: string, secret_words: list).
This function should return inner function check.

The function check compares the values of its
arguments with password and secret_words:
the password must match completely, secret_words may be misspelled (just one element).

Password should contain at least 6 symbols including
one uppercase letter, one lowercase letter,
special character and one number.

Перевірка функції порівнює значення її
аргументи з паролем і секретними_словами:
пароль має збігатися повністю, секретні_слова можуть бути написані з помилкою (лише один елемент).

Пароль повинен містити не менше 6 символів включно
одна велика літера, одна мала літера,
спеціальний символ і одне число.

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
    def equalsWord(words, secret_words):
        k = len(secret_words)

        for word in secret_words:
            if word in words:
                k -= 1
                words.remove(word)
        return True if k == 1 or k == 0 else False

    def check(pswrd: str, words: list):
        if len(words) != len(secret_words):
            # print("LEN", words, secret_words)
            return False
        elif pswrd != password:
            # print("pswrd_check", pswrd,"!=",password)
            return False
        elif equalsWord(words, secret_words):

            return True
        else:
            # print("Not equals", words, secret_words)
            return False

    # print("".join(secret_words))
    lnPassword = len(password) >= 6
    notUpper = not password.isupper()
    notLower = not password.islower()
    notAlpha = not password.isalpha()
    notAlNum = not password.isalnum()

    # print("lnPassword", lnPassword)
    # print("notLower", notLower)
    # print("notUpper", notUpper)
    # print("notAlpha", notAlpha)
    # print("notNum", notAlNum)
    # print(lnPassword and notLower and notUpper and notAlpha and notAlNum)

    if lnPassword and notLower and notUpper and notAlpha and notAlNum:
        return check
    else:
        raise ValueError


if __name__ == '__main__':
    tom = create_account("Tom", "Qwerty1_", ["1", "word"])
    check1 = tom("Qwerty1_", ["1", "word"])
    print(check1)
    check2 = tom("Qwerty1_", ["word"])
    print(check2)
    check3 = tom("Qwerty1_", ["word", "2"])
    print("ch3 = ", check3)
    check4 = tom("Qwerty1!", ["word", "12"])
    print(check4)

    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_1_true))
    # True
    # True
    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_2_true))
    # True
    # True
    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_3_true))
    # True
    # True
    # print('check' in list(get_names(create_account)))
    # True
    # True
    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_4_true))
    # True
    # True
    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_5_true))
    # True
    # True
    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_6_true))
    # True
    # True
    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_7_false))
    # False
    # True
    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_8_false))
    # False
    # True
    # val1 = create_account("123", "qQ1!45", initial_arr)
    # print(val1("qQ1!45", checked_arr_9_false))
    # False
    # True
    # try:
    #     val1 = create_account("123", "qQ1345", initial_arr)
    # except ValueError:
    #     print("Raises ValueError")
    # Raises
    # ValueError
    # print(check1, check2, check3, check4)
    # True
    # False
    # True
    # False
    # True
    # True
    # True
    # True
    # user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
    # print(user2("yu6r*Tt5", ["abc3", "word1", "list"]))
    # True
    # True
    # user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
    # print(user2("yu6r*Tt5", ["abc3", "word1", "zzzzzz"]))
    # True
    # True
    # user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
    # print(user2("yu6r*Tt5", ["abc3", "abc3", "abc3"]))
    # False
    # True
    # user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
    # print(user2("yu6r*Tt5", ["word1", "zzzz", "z"]))
    # False
    # True
    # user3 = create_account("User", "MmKk*9kj", ["1", "2", "1"])
    # print(user3("MmKk*9kj", initial_arr))
    # True
    # True
    # try:
    #     simple_user = create_account("A", "Aa!1", ["word"])
    # except ValueError:
    #     print("Raises ValueError")
    # Raises
    # ValueError
    simple_user = create_account("A", "Aa!190", ["word"])
    print(simple_user("Aa!190", ["word"]))
    # True
    # True
