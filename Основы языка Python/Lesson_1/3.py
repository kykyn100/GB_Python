print('Программа для расчета выражения n + nn + nnn, '
      'где n-число введеное пользователем ')
n = input('Введите число: ')
print(f'Выражение {n} + {n + n} + {n + n + n} = '
      f'{int(n)+int(n + n)+int(n + n + n)}')
