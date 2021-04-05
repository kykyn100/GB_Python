class ZeroExcept(Exception):

    def __init__(self, txt):
        self.txt = txt


a = input('Введите делимое "a": ')
b = input('Введите делитель "b": ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise ZeroExcept('Ну нельзя делить на 0 !')
    c = a / b
except ValueError:
    print('Нужно вводить числа')
except ZeroExcept as my_err:
    print(my_err)
else:
    print(f'Результат деления: {c}')