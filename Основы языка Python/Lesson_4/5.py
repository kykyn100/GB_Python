from functools import reduce


def summer(first, second):
    return first + second


print(reduce(summer, [i for i in range(100, 1001) if i % 2 == 0]))
