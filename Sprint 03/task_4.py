"""Create function-generator divisor that should return all divisors of the positive number.
If there are no divisors left function should return None.
three = divisor(3)
next(three) => 1
next(three) => 3
next(three) => None"""


def divisor(num: int):
    for i in range(1, num + 1):
        # print("i= ", i)
        if num % i == 0:
            yield i
    while True:
        yield None


if __name__ == "__main__":
    three = divisor(3)
    print(next(three))
    print(next(three))
    print(next(three))
    print(next(three))
