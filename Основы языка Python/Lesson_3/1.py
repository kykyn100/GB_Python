def division_num(num1, num2):
    try:
        num1 = int(input('Введите делимое: '))
        num2 = int(input('Введите делитель: '))
    except ValueError:
        print('Введите число!')
   try:
        division_result = num1 / num2
    except ZeroDivisionError:
        print('На 0 делить нельзя!')
        return division_result

result = division_num(num1, num2)
print(result)
