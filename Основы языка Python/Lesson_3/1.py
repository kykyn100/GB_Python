# Коментарий для создания PR
def division_num(num1, num2):
    try:
        division_result = num1 / num2
    except ZeroDivisionError:
        return 'На 0 делить нельзя!'
    return division_result


try:
    div1 = int(input('Введите делимое: '))
    div2 = int(input('Введите делитель: '))
except ValueError:
    print('Нужно ввести число!')

result = division_num(div1, div2)
print(result)
