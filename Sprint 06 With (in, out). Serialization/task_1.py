"""
Create function find(file, key)
This function parses json-file and returns all unique values of the key.

1.json:
[{"name": "user_1”, "password": "pass_1”},
{"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
find("1.json", "password") returns ["pass_1", "qwerty"]

2.json:
[{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]

3.json:
{"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
find("3.json", "password") returns ["1234qweQWE"]

Answer:(penalty regime: 0 %)
"""
import json


def get_data_from_json(file):
    folder = "Test_data/"
    # folder = ""
    with open(folder + file) as json_file:
        data = json.load(json_file)
        return data


def find(file, _key):
    def add_uniq(data):
        if isinstance(data, dict):
            data = [{key: value} for key, value in data.items()]
        elif isinstance(data, str):
            return

        for dct in data:
            for key, value in dct.items():
                if isinstance(value, list):
                    for each in value:
                        if isinstance(each, dict):
                            add_uniq(each)
                        elif key == _key:
                            unique_values.add(each)
                elif isinstance(value, dict):
                    add_uniq(value)
                elif key == _key:
                    unique_values.add(value)
        return

    data = get_data_from_json(file)
    unique_values = set()
    add_uniq(data)

    return list(unique_values)


if __name__ == "__main__":
    print(find("without_pass.json", 'password') == [])
    print(find("without_pass.json", 'password'))
    # []
    # ## =============================
    import collections

    actual = find("array_pass.json", "password")
    expected = ['56', '_00_']
    print(collections.Counter(actual) == collections.Counter(expected))
    print(actual)
    # expected = ['56', '_00_']
    # #
    # # ## =============================
    # import collections
    #
    # actual = find("one_user_one_pass.json", "password")
    #
    # expected = ['_00_']
    # print(collections.Counter(actual) == collections.Counter(expected))
    # print(actual)
    # # # True
    #
    # # # =============================
    # # import collections
    # #
    # # actual = find("one_user_one_pass.json", "password")
    # # expected = ['_00_']
    # # print(collections.Counter(actual) == collections.Counter(expected))
    # # # True
    #
    # # # # =============================
    # # import collections
    # #
    # # actual = find("one_user_array_pass.json", "password")
    # # expected = ['try', '_00_']
    # # print(collections.Counter(actual) == collections.Counter(expected))
    # # print(actual)
    # # # True
    #
    # # # # =============================
    # import collections
    #
    # actual = find("5.json", "username")
    # expected = ['Nick', 'Tom1', 'Tom', 'OneMore']
    # print(collections.Counter(actual) == collections.Counter(expected))
    # print(actual)
    # # True
    #
    # # # # =============================
    # import collections
    #
    # actual = find("2.json", "password")
    # expected = ['1234qweQWE', 'pass_1 ', 'qwerty ']
    # print(collections.Counter(actual) == collections.Counter(expected))
    # print(actual)
    # True

    # # # # # =============================
    #
    # from random import choices
    # from string import ascii_letters, digits
    # import collections
    #
    # letters_and_digits = ascii_letters + digits
    # password = ''.join(choices(letters_and_digits, k=12))
    # expected = [password]
    # data = {
    #     "name": "Random",
    #     "password": password
    # }
    # with open("Test_data/random_test_data.json", "w") as write_file:
    #     json.dump(data, write_file)
    # actual = find("random_test_data.json", "password")
    # print(collections.Counter(actual) == collections.Counter(expected))
    # # True
