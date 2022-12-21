"""
As input data, you have a string that consists of words that have duplicated characters at the end of it.

All duplications may be in the next format:

wordxxxx
wordxyxyxy
wordxyzxyzxyz
, where x, xy or xyz repeated ending of the word

Using re module write function pretty_message() that remove all duplications

For example:
Test	                    Result
data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data))
This is echo string. Replace repeated groups of symbols

data = "Another input data string"
print(pretty_message(data))
Another input data string
"""
# https://techrocks.ru/2019/09/09/regex-isnt-as-hard-as-you-think-2/

import re


def pretty_message(string):
    lst = re.findall(r"(\w+)\1+", string, flags=0)
    # print(lst)
    while len(lst) > 0:
        string = re.sub(r"(\w+)\1+", r"\1", string)
        lst = re.findall(r"(\w+)\1+", string, flags=0)
    return string


data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data))  # This is echo string. Replace repeated groups of symbols
