def my_func1(x, y):
    result = x ** y
    return result


def my_func2(x, y):
    result = None
    if y < 0:
        z = x
        for i in range(1, abs(y)):
            z *= x
        result = 1 / z
    else:
        z = x
        for i in range(1, y):
            z *= x
        result = z
    return result


num1 = int(input('Введите основание: '))
num2 = int(input('Введите показатель степени: '))

num_result = my_func1(num1, num2)
print(num_result)

num_result = my_func2(num1, num2)
print(num_result)

