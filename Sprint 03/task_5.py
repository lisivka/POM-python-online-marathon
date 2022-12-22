"""Create decorator logger. The decorator should print to
the console information about function's name
and all its arguments separated with ','
for the function decorated with logger.

Create function concat with any numbers
of any arguments which concatenates arguments
and apply logger decorator for this function.

For example
print(concat(2, 3)) display
Executing of function concat with arguments 2, 3...
23

print(concat('hello', 2)) display
Executing of function concat with arguments hello, 2...
hello2

print(concat (first = 'one', second = 'two')) display
Executing of function concat with arguments one, two...
onetwo
"""


def logger(func):
    def args_kwargs(*args, **kwargs):
        lst_arg = [str(element) for element in args]
        lst_kwargs = [str(value) for key, value in kwargs.items()]
        comma = ", " if lst_arg and lst_kwargs else ""
        arguments = ", ".join(lst_arg) +comma+ ", ".join(lst_kwargs)
        recursive_func = func(*args, **kwargs)

        # print(f"Executing of function {func.__name__} with arguments {lst_arg}...", end=" ")
        print(f"Executing of function {func.__name__} with arguments {arguments}...", end="\n")
        return recursive_func

    # print(f"Executing of function {func.__name__} with arguments ""...", end=" ")

    return args_kwargs


@logger
def concat(*args, **kwargs):
    lst_arg = [str(element) for element in args]
    lst_kwargs = [str(value) for key, value in kwargs.items()]
    arguments = "".join(lst_arg) + "".join(lst_kwargs)
    return arguments


@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)


print(concat(2, 3))
print(sum(2, 3))
print(concat('hello', 2))
print(concat(first='one', second='two'))
print("------------------")
print(concat(1))
# Executing of function concat with arguments 1...
# 1
# None
print(concat('first string', second=2, third='second string'))
# Executing of function concat with arguments first string, 2, second string...
# first string2second string
# None
# print(concat('first string', {'first kwarg' :0, 'second kwarg': 'second kwarg'}))
# Executing of function concat with arguments first string, {'first kwarg': 0, 'second kwarg': 'second kwarg'}...
# first string{'first kwarg': 0, 'second kwarg': 'second kwarg'}
# None
# print(sum(2,3))
# Executing of function sum with arguments 2, 3...
# 5
# ***Run error***
# Traceback (most recent call last):
#   File "__tester__.python3", line 31, in <module>
#     print(sum(2,3))
# TypeError: 'NoneType' object is not callable


# a ="Executing of function concat with arguments first string, 2, second string...first string2second string"
# b ="Executing of function concat with arguments first string2, second string...
# first string2second string"
