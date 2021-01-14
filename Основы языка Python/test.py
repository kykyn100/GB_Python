from itertools import count


def fact(n):
    if n == 0:
        yield 1
    else:
        for z in range(1, n + 1):
            result = 1
            for i in range(1, z + 1):
                result *= i
            yield result


num = int(input('Факториал каокго числа необходимо вычислить? '))

for el in fact(num):
    print(el)