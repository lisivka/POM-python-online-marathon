"""
As input data, you have a list of strings.

Write a method double_string() for counting the number of strings from the list,
represented in the form of the concatenation of two strings from this arguments  list

For example:
Test	Result
data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data))
# >>>3
data = ['aa', 'abc', 'qwerqwer']
print(double_string(data))
# >>>0

"""


def double_string(data: list):
    counter = 0
    data_set=set(data)
    for i in data_set:
        for j in data_set:
            if unit + unit in data:
                counter += data.count(unit + unit)

    data_set = [i+j  for i in data]
    print(data_set)
    for unit in data:
        if unit + unit in data:
            print(unit)
            counter += data.count(unit + unit)

    # counter_list = [data.count(unit+unit) for unit in data if unit+unit in data]
    # print(counter_list)
    return counter
    # return sum(counter_list)


# data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data))
