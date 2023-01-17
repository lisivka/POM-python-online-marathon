"""
Create function file_parser. If function is called with 2 arguments
it must count the number of occurrences string in a file,
in case of 3 arguments it must replace string in a file to new string

first argument - path to file
second argument - find string
third argument - replace string
Function must returned string with count of occurrences or count of replaced strings

Example:

file_parser("file.txt", 'x', 'o')-> Replaced 8 strings
file_parser("file.txt", 'o') -> Found 8 strings
Please, create class ParsesTest and write unittest for file_parser function uses mock object
"""

import unittest


def file_parser(file, find_str, replace_str=None):
    with open(file, 'r') as f:
        data = f.read()
    count = data.count(find_str)
    if count > 0 and replace_str is not None:
        data = data.replace(find_str, replace_str)
        with open(file, 'w') as f:
            f.write(data)
        return f"Replaced {count} strings"
    else:
        return f"Found {count} strings"


# class ParserTest(unittest.TestCase):
#     pass

print(file_parser('file.txt', 'argument'))
print(file_parser('file.txt', 'argumen', "argument"))
# print(file_parser('parser.txt', 'better'))
